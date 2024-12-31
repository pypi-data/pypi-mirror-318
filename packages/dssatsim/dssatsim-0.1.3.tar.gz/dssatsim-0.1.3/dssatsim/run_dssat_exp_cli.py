import argparse
import json
import os
from datetime import datetime
import pandas as pd
from itertools import chain
from DSSATTools import (
    Crop, SoilProfile, Weather, Management, DSSAT, TabularSubsection,
)
import dssatsim.utils as ut
from dssatsim.explain_dssat_outputs import explain_summary_out
from dssatsim.envs import (
    DB_VARS, MINIMUM_REQUIRED_FARMER_INPUTS, ASSUMPTIONS,
    OUTDIR, INSTI_CODE, SUMMARY_OUT_AS_JSON_NAN, DSSAT_NA_VALUE,
    CROP_NAMES_TO_CROP_VARIETIES, CROP_VARIETIES_TO_CULTIVAR_CODES
)
pd.options.mode.chained_assignment = None

# Constants
DB_PARAMS = {
    'dbname': DB_VARS['DB_NAME'],
    'user': DB_VARS['DB_USER'],
    'password': DB_VARS['DB_PASSWORD'],
    'host': DB_VARS['DB_HOST'],
    'port': DB_VARS['DB_PORT']
}


def is_simulation_possible(input_data):
    for min_input in MINIMUM_REQUIRED_FARMER_INPUTS:
        got = input_data.get(min_input, None)

        if got is None:
            return False
        
        if isinstance(got, str) and got == "-99":
            return False

        if isinstance(got, int) and got == -99:
            return False
        
        if isinstance(got, list) :
            is_irrigation_applied = input_data.get("is_irrigation_applied", None)
            if is_irrigation_applied.lower() == "yes" and -99 in list(chain.from_iterable(got)):
                return False
    return True


def setup_crop_module(crop_name, crop_variety):
    crop_name = crop_name.title()

    if crop_name not in CROP_NAMES_TO_CROP_VARIETIES.keys():
        raise ValueError(f"Crop name `{crop_name}` is not supported.")
    if crop_variety not in CROP_VARIETIES_TO_CULTIVAR_CODES.keys():
        raise ValueError(f"Crop variety `{crop_variety}` is not supported.")
    
    crop_cultivar_props = CROP_VARIETIES_TO_CULTIVAR_CODES[crop_variety]

    dssat_crop_module = Crop(
        crop_name=crop_name,
        cultivar_code=crop_cultivar_props['@VAR#'],
    )

    for prop, val in crop_cultivar_props.items():
        if prop in ["@VAR#", "ECO#"]:
            continue
        dssat_crop_module.cultivar[prop] = val

    return dssat_crop_module


def setup_irrigation_table(irr_apps_list):
    schedule = pd.DataFrame(irr_apps_list, columns=["IDATE", "IRVAL"]) # IRVAL is in mm
    schedule["IDATE"] = pd.to_datetime(schedule["IDATE"])
    schedule["IDATE"] = schedule.IDATE.dt.strftime('%y%j')
    schedule["IROP"] = ASSUMPTIONS["irrigation_operation_code"]
    schedule = schedule[["IDATE", "IROP", "IRVAL"]]
    return TabularSubsection(schedule)

def setup_weather_module(planting_date, latitude, longitude, elevation):
    
    year = int(planting_date.split("-")[0])

    extracted_wth_res = ut.location_to_WTH_file(
        DB_PARAMS, 
        target_lat=latitude, 
        target_lon=longitude, 
        year=year, 
        outdir=OUTDIR, 
        institution_code=INSTI_CODE
    )

    weather_df = extracted_wth_res['wth_table_df']
    weather_df = weather_df[['TMIN', 'TMAX', 'RAIN', 'SRAD']]

    # handling missing rows to weather_df to account for the last day of December
    missing_rows_for_last_day_december = [{
        "TMIN": weather_df["TMIN"].iloc[-30:].min(), # last 30 days/i.e. December days only
        "TMAX": weather_df["TMAX"].iloc[-30:].max(), 
        "RAIN": weather_df["RAIN"].iloc[-30:].mean(), 
        "SRAD": weather_df["SRAD"].iloc[-30:].mean()
    }]
    missing_rows_df = pd.DataFrame(missing_rows_for_last_day_december)
    weather_df = pd.concat([weather_df, missing_rows_df], ignore_index=True)
    weather_df = pd.concat([weather_df, weather_df], ignore_index=True)

    # some assumption is being made here: 
    # - weather year for 2024 is the same as 2023
    # - currently we are only simulating for 2023, but then we added Wheat, which is a winter crop and thus requires weather data for 2024
    # - Of course, this was done for testing purposes.
    # Feb 29th, 2024 is the 425th day of the 2023 through 2024 span
    # Insert a new row between the neighboring rows of the 424th day
    day_424_row = pd.DataFrame([weather_df.iloc[424]])
    weather_df = pd.concat([weather_df.iloc[:424], day_424_row, weather_df.iloc[424:]], ignore_index=True)

    weather_df["DATES"] = pd.date_range(f"{year}-01-01", f"{year+1}-12-31")
    weather_df = weather_df.set_index("DATES")

    dssat_weather_module = Weather(
        df=weather_df,
        pars={'TMIN': 'TMIN', 'TMAX': 'TMAX', 'RAIN': 'RAIN', 'SRAD': 'SRAD',},
        lat=latitude,
        lon=longitude,
        elev=elevation,
        tav=ASSUMPTIONS["avg_annual_soil_temperature"],
        amp=ASSUMPTIONS["amplitude_soil_temperature"],
    )

    return dssat_weather_module


def setup_soil_module(lat, lon):
    extracted_sol_res = ut.location_to_SOL_file(
        db_params=DB_PARAMS, 
        target_lat=lat, 
        target_lon=lon, 
        outdir=OUTDIR, 
    )
    sol_fpath = extracted_sol_res['sol_fpath']
    soil_profile_name = extracted_sol_res['soil_profile_name']

    dssat_soil_module = SoilProfile(file=sol_fpath, profile=soil_profile_name)

    return dssat_soil_module


def was_fertilizer_applied(fert_apps_items):
    return any([len(fert_apps_items[key]) > 0 for key in fert_apps_items.keys()])

def setup_fertilizer_table(fert_apps_items):

    fert_details_assumptions = {
        "FMCD": ASSUMPTIONS["fertilizer_material_code"],
        "FACD": ASSUMPTIONS["fertilizer_application_code"],
        "FDEP": ASSUMPTIONS["fertilizer_depth"], 
        "FAMC": ASSUMPTIONS["fertilizer_Ca"], 
        "FAMO": ASSUMPTIONS["fertilizer_other_elements_applied"], 
        "FOCD": ASSUMPTIONS["fertilizer_other_elements_code"], 
        "FERNAME": ASSUMPTIONS["fertilizer_name"], 
    }

    # see https://github.com/daquinterop/Py_DSSATTools/blob/29da1eea7d2bf2d03a2be7c4534aef7e5798bcca/DSSATTools/management.py#L214
    main_columns = ["FDATE", "FMCD", "FACD", "FDEP", "FAMN", "FAMP", "FAMK", "FAMC", "FAMO", "FOCD", "FERNAME"]

    n_apps_df = pd.DataFrame(fert_apps_items["nitrogen_fertilizer_application"], columns=['FDATE', 'FAMN'])
    p_apps_df = pd.DataFrame(fert_apps_items["phosphorus_fertilizer_application"], columns=['FDATE', 'FAMP'])
    k_apps_df = pd.DataFrame(fert_apps_items["potassium_fertilizer_application"], columns=['FDATE', 'FAMK'])

    npk_ferts_df = pd.merge(n_apps_df, p_apps_df, on='FDATE', how='outer')
    npk_ferts_df = pd.merge(npk_ferts_df, k_apps_df, on='FDATE', how='outer')
    npk_ferts_df = npk_ferts_df.fillna(0)

    schedule = npk_ferts_df.copy()
    schedule["FDATE"] = pd.to_datetime(schedule["FDATE"])
    schedule["FDATE"] = schedule.FDATE.dt.strftime('%y%j')

    for col, val in fert_details_assumptions.items():
        schedule[col] = val

    schedule = schedule[main_columns]

    return TabularSubsection(schedule)


def setup_management_module(planting_date, is_irrigation_applied, irrigation_application, fertilizer_application):

    dssat_management_module = Management(
        planting_date=datetime.strptime(planting_date, "%Y-%m-%d"),
        sim_start=ASSUMPTIONS["simulation_start"],  
        emergence_date=ASSUMPTIONS["emergence_date"], 
        initial_swc=ASSUMPTIONS["initial_swc"], 
        harvest=ASSUMPTIONS["harvest_management_option"], 
        organic_matter=ASSUMPTIONS["organic_matter_management_option"], 
    )

    if is_irrigation_applied.lower() == "no":
        dssat_management_module.simulation_controls["IRRIG"] = "N"
    else:
        dssat_management_module.simulation_controls["IRRIG"] = "R"
        dssat_management_module.irrigation['table'] = setup_irrigation_table(irrigation_application)

    if was_fertilizer_applied(fertilizer_application):
        print("Detected Fertilizer application")
        dssat_management_module.fertilizers['table'] = setup_fertilizer_table(fertilizer_application)

        dssat_management_module.simulation_controls["FERTI"] = "R"

        if was_fertilizer_applied({"nitrogen_fertilizer_application": fertilizer_application["nitrogen_fertilizer_application"]}):
            dssat_management_module.simulation_controls["NITRO"] = "Y"
        if was_fertilizer_applied({"phosphorus_fertilizer_application": fertilizer_application["phosphorus_fertilizer_application"]}):
            dssat_management_module.simulation_controls["PHOSP"] = "Y"
        if was_fertilizer_applied({"potassium_fertilizer_application": fertilizer_application["potassium_fertilizer_application"]}):
            dssat_management_module.simulation_controls["POTAS"] = "Y"

    else:
        dssat_management_module.simulation_controls["FERTI"] = "N"


    return dssat_management_module


def exec(input_file, output_file=None, remove_temp_files=True):

    if isinstance(input_file, dict):
        input_data = input_file
    else:
        input_file = os.path.abspath(input_file)
        with open(input_file, 'r', encoding='utf-8') as f:
            input_data = json.load(f)

    # Check if simulation is possible
    if not is_simulation_possible(input_data):
        return None, SUMMARY_OUT_AS_JSON_NAN
    
    # extract fertilizer applications, or initialize as empty lists otherwise
    fertilizer_application = {
        "nitrogen_fertilizer_application": input_data.get("nitrogen_fertilizer_application", []),
        "phosphorus_fertilizer_application": input_data.get("phosphorus_fertilizer_application", []),
        "potassium_fertilizer_application": input_data.get("potassium_fertilizer_application", []),
    }

    # 1. Prepare Weather
    dssat_weather_module = setup_weather_module(
        input_data["planting_date"],
        input_data["latitude"],
        input_data["longitude"],
        input_data["elevation"],
    )

    # 2. Prepare Soil
    dssat_soil_module = setup_soil_module(input_data["latitude"], input_data["longitude"])

    # 3. Prepare Crop module
    dssat_crop_module = setup_crop_module(input_data["crop_name"], input_data["crop_variety"])

    # 4. Prepare the management
    dssat_management_module = setup_management_module(
        planting_date=input_data["planting_date"],
        is_irrigation_applied=input_data["is_irrigation_applied"],
        irrigation_application=input_data["irrigation_application"],
        fertilizer_application=fertilizer_application,
    )

    # Run DSSAT experiment
    dssat = DSSAT()
    dssat.setup()
    dssat.run(
        soil=dssat_soil_module, 
        weather=dssat_weather_module, 
        crop=dssat_crop_module, 
        management=dssat_management_module,
    )

    # Finalize
    if dssat.output is None:
        print(f"Simulation `{input_data['experiment_name']}` did not run successfully")
    else:
        summary_out_fpath = ut.retrieve_fout_path(code="Summary")
        if not os.path.exists(summary_out_fpath):
            print(f"Summary file not found at {summary_out_fpath}")
            explanations = SUMMARY_OUT_AS_JSON_NAN
        else:
            explanations, _ = explain_summary_out(summary_out_fpath, output_file)

    dssat.close()
    
    if remove_temp_files: ut.clean_up_folder(OUTDIR)

    return output_file, explanations

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Run a DSSAT simulation based on input JSON file.")
    parser.add_argument('input_file', type=str, help="Path to the input JSON file.")

    args = parser.parse_args()
    exec(args.input_file)
