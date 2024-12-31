import os
from dotenv import load_dotenv

BASE_DIR = os.path.abspath(os.path.dirname(__file__))
STATIC_DIR = os.path.join(BASE_DIR, "static")
SERVERLESS_DB_DIR = os.path.join(BASE_DIR, "serverlessdb")
ALL_DSSAT_CDE_FILES = os.path.join(STATIC_DIR, "ALL_DSSAT_CDE_FILES.csv")
DSSAT_CROP_COEFFS_METADATA = os.path.join(STATIC_DIR, "CUL_SPE_ECO_COEFFS_DEFINITIONS.csv")
OFFICIAL_DSSAT_CROP_CODES = os.path.join(STATIC_DIR, "OFFICIAL_DSSAT_CROP_CODES.csv")

OUTDIR = os.path.join(os.path.dirname(__file__), "iopairs")
INSTI_CODE = "AGXQ"
SUMMARY_OUT_AS_JSON_NAN = {"simulation_results": "impossible"}

load_dotenv()

DB_VARS = {
    'DB_USER': os.getenv("DB_USER"),
    'DB_PASSWORD': os.getenv("DB_PASSWORD"),
    'DB_HOST':os.getenv("DB_HOST"),
    'DB_PORT':os.getenv("DB_PORT"),
    'DB_NAME':os.getenv("DB_NAME"),
}

MISSING_NA_VALUE = "-99"
DSSAT_NA_VALUE = "-99"


REMOTE_OUT_DIR = os.getenv("REMOTE_OUT_DIR")

WTH_COLUMNS = ['@DATE', 'SRAD', 'TMAX', 'TMIN', 'RAIN', 'DEWP', 'WIND', 'PAR', 'EVAP', 'RHUM']

DATA_TYPES_TO_DB_TABLES = {
    "sol":"US_SOIL_DATA_TABLE_10km",
    "wth": "KALAMAZOO_3KFARMS_WEATHER_DATA_TABLE_1km",
    "evapotranspiration": "KALAMAZOO_3KFARMS_EVAPOTRANS_DATA_TABLE_500m",
    "vegetation": "KALAMAZOO_3KFARMS_VEGETATION_DATA_TABLE_250m",
}

ABBREV_IN_SOL_FILE = { 
    'soil_profile_name': "soil_profile_name",
    'soil_data_source': "soil_data_source",
    'soil_texture': "soil_texture",
    'soil_depth': "soil_depth",
    'soil_series_name': "soil_series_name",

    'soil_site_name': "SITE",
    'soil_country_name': "COUNTRY",
    'latitude': "LAT",
    'longitude': "LON",
    'soil_classification_family': "SCS Family",

    'soil_color': "SCOM",
    'soil_albedo': "SALB",
    'soil_evalopration_limit': "SLU1",
    'soil_drainage_coefficient': "SLDR",
    'soil_runoff_curve_no': "SLRO",
    'soil_mineralization_factor': "SLNF",
    'soil_photosynthesis_factor': "SLPF",
    'soil_ph_in_buffer_determination_code': "SMHB",
    'soil_phosphorus_determination_code': "SMPX",
    'soil_potassium_determination_code': "SMKE",

    'soil_depth_bottom': "SLB",
    'soil_master_horizon': "SLMH",
    'soil_lower_limit': "SLLL",
    'soil_upper_limit_drained': "SDUL",
    'soil_upper_limit_saturated': "SSAT",
    'soil_root_growth_factor': "SRGF",
    'soil_sat_hydraulic_conductivity': "SSKS",
    'soil_bulk_density_moist': "SBDM",
    'soil_organic_carbon': "SLOC",
    'soil_clay': "SLCL",
    'soil_silt': "SLSI",
    'soil_coarse_fraction': "SLCF",
    'soil_total_nitrogen': "SLNI",
    'soil_ph_in_water': "SLHW",
    'soil_ph_in_buffer': "SLHB",
    'soil_cation_exchange_capacity': "SCEC",
    'soil_sadc': "SADC",

    'soil_depth_bottom_5cm': "SLB_5cm",
    'soil_master_horizon_5cm': "SLMH_5cm",
    'soil_lower_limit_5cm': "SLLL_5cm",
    'soil_upper_limit_drained_5cm': "SDUL_5cm",
    'soil_upper_limit_saturated_5cm': "SSAT_5cm",
    'soil_root_growth_factor_5cm': "SRGF_5cm",
    'soil_sat_hydraulic_conductivity_5cm': "SSKS_5cm",
    'soil_bulk_density_moist_5cm': "SBDM_5cm",
    'soil_organic_carbon_5cm': "SLOC_5cm",
    'soil_clay_5cm': "SLCL_5cm",
    'soil_silt_5cm': "SLSI_5cm",
    'soil_coarse_fraction_5cm': "SLCF_5cm",
    'soil_total_nitrogen_5cm': "SLNI_5cm",
    'soil_ph_in_water_5cm': "SLHW_5cm",
    'soil_ph_in_buffer_5cm': "SLHB_5cm",
    'soil_cation_exchange_capacity_5cm': "SCEC_5cm",
    'soil_sadc_5cm': "SADC_5cm",

    'soil_depth_bottom_15cm': "SLB_15cm",
    'soil_master_horizon_15cm': "SLMH_15cm",
    'soil_lower_limit_15cm': "SLLL_15cm",
    'soil_upper_limit_drained_15cm': "SDUL_15cm",
    'soil_upper_limit_saturated_15cm': "SSAT_15cm",
    'soil_root_growth_factor_15cm': "SRGF_15cm",
    'soil_sat_hydraulic_conductivity_15cm': "SSKS_15cm",
    'soil_bulk_density_moist_15cm': "SBDM_15cm",
    'soil_organic_carbon_15cm': "SLOC_15cm",
    'soil_clay_15cm': "SLCL_15cm",
    'soil_silt_15cm': "SLSI_15cm",
    'soil_coarse_fraction_15cm': "SLCF_15cm",
    'soil_total_nitrogen_15cm': "SLNI_15cm",
    'soil_ph_in_water_15cm': "SLHW_15cm",
    'soil_ph_in_buffer_15cm': "SLHB_15cm",
    'soil_cation_exchange_capacity_15cm': "SCEC_15cm",
    'soil_sadc_15cm': "SADC_15cm",

    'soil_depth_bottom_30cm': "SLB_30cm",
    'soil_master_horizon_30cm': "SLMH_30cm",
    'soil_lower_limit_30cm': "SLLL_30cm",
    'soil_upper_limit_drained_30cm': "SDUL_30cm",
    'soil_upper_limit_saturated_30cm': "SSAT_30cm",
    'soil_root_growth_factor_30cm': "SRGF_30cm",
    'soil_sat_hydraulic_conductivity_30cm': "SSKS_30cm",
    'soil_bulk_density_moist_30cm': "SBDM_30cm",
    'soil_organic_carbon_30cm': "SLOC_30cm",
    'soil_clay_30cm': "SLCL_30cm",
    'soil_silt_30cm': "SLSI_30cm",
    'soil_coarse_fraction_30cm': "SLCF_30cm",
    'soil_total_nitrogen_30cm': "SLNI_30cm",
    'soil_ph_in_water_30cm': "SLHW_30cm",
    'soil_ph_in_buffer_30cm': "SLHB_30cm",
    'soil_cation_exchange_capacity_30cm': "SCEC_30cm",
    'soil_sadc_30cm': "SADC_30cm",

    'soil_depth_bottom_60cm': "SLB_60cm",
    'soil_master_horizon_60cm': "SLMH_60cm",
    'soil_lower_limit_60cm': "SLLL_60cm",
    'soil_upper_limit_drained_60cm': "SDUL_60cm",
    'soil_upper_limit_saturated_60cm': "SSAT_60cm",
    'soil_root_growth_factor_60cm': "SRGF_60cm",
    'soil_sat_hydraulic_conductivity_60cm': "SSKS_60cm",
    'soil_bulk_density_moist_60cm': "SBDM_60cm",
    'soil_organic_carbon_60cm': "SLOC_60cm",
    'soil_clay_60cm': "SLCL_60cm",
    'soil_silt_60cm': "SLSI_60cm",
    'soil_coarse_fraction_60cm': "SLCF_60cm",
    'soil_total_nitrogen_60cm': "SLNI_60cm",
    'soil_ph_in_water_60cm': "SLHW_60cm",
    'soil_ph_in_buffer_60cm': "SLHB_60cm",
    'soil_cation_exchange_capacity_60cm': "SCEC_60cm",
    'soil_sadc_60cm': "SADC_60cm",

    'soil_depth_bottom_100cm': "SLB_100cm",
    'soil_master_horizon_100cm': "SLMH_100cm",
    'soil_lower_limit_100cm': "SLLL_100cm",
    'soil_upper_limit_drained_100cm': "SDUL_100cm",
    'soil_upper_limit_saturated_100cm': "SSAT_100cm",
    'soil_root_growth_factor_100cm': "SRGF_100cm",
    'soil_sat_hydraulic_conductivity_100cm': "SSKS_100cm",
    'soil_bulk_density_moist_100cm': "SBDM_100cm",
    'soil_organic_carbon_100cm': "SLOC_100cm",
    'soil_clay_100cm': "SLCL_100cm",
    'soil_silt_100cm': "SLSI_100cm",
    'soil_coarse_fraction_100cm': "SLCF_100cm",
    'soil_total_nitrogen_100cm': "SLNI_100cm",
    'soil_ph_in_water_100cm': "SLHW_100cm",
    'soil_ph_in_buffer_100cm': "SLHB_100cm",
    'soil_cation_exchange_capacity_100cm': "SCEC_100cm",
    'soil_sadc_100cm': "SADC_100cm",

    'soil_depth_bottom_200cm': "SLB_200cm",
    'soil_master_horizon_200cm': "SLMH_200cm",
    'soil_lower_limit_200cm': "SLLL_200cm",
    'soil_upper_limit_drained_200cm': "SDUL_200cm",
    'soil_upper_limit_saturated_200cm': "SSAT_200cm",
    'soil_root_growth_factor_200cm': "SRGF_200cm",
    'soil_sat_hydraulic_conductivity_200cm': "SSKS_200cm",
    'soil_bulk_density_moist_200cm': "SBDM_200cm",
    'soil_organic_carbon_200cm': "SLOC_200cm",
    'soil_clay_200cm': "SLCL_200cm",
    'soil_silt_200cm': "SLSI_200cm",
    'soil_coarse_fraction_200cm': "SLCF_200cm",
    'soil_total_nitrogen_200cm': "SLNI_200cm",
    'soil_ph_in_water_200cm': "SLHW_200cm",
    'soil_ph_in_buffer_200cm': "SLHB_200cm",
    'soil_cation_exchange_capacity_200cm': "SCEC_200cm",
    'soil_sadc_200cm': "SADC_200cm",

    } 

CROP_NAMES_TO_CROP_VARIETIES = {
    "Maize": ["MZ GREAT LAKES 482", "MZ GREAT LAKES 582", "MZ GREAT LAKES 582 KBS"],
    "Soybean": ["SB MATURITY GROUP 2"],
    "Wheat": ["WH NEWTON (Chelsea soft white)"],
}

CROP_VARIETIES_TO_CULTIVAR_CODES = {
    # Maize
    "MZ GREAT LAKES 482": {
        "@VAR#": "IB0090",
        "ECO#": "IB0001",
        "P1": 240.0,
        "P2": 0.7,
        "P5": 990.0,
        "G2": 907.0,
        "G3": 8.8,
        "PHINT": 38.9,
    },
    "MZ GREAT LAKES 582": {
        "@VAR#": "IB0089",
        "ECO#": "IB0001",
        "P1": 200.0,
        "P2": 0.7,
        "P5": 750.0,
        "G2": 750.0,
        "G3": 8.6,
        "PHINT": 38.9,
    },
    "MZ GREAT LAKES 582 KBS": {
        "@VAR#": "IB0093",
        "ECO#": "IB0001",
        "P1": 180.0,
        "P2": 0.7,
        "P5": 750.0,
        "G2": 750.0,
        "G3": 8.6,
        "PHINT": 38.9,
    },

    # Soybean. e.g. see SBCRO48.CUL
    "SB MATURITY GROUP 2" : {
        "@VAR#": "990002",
        "ECO#": "SB0201",
        "CSDL": 13.59,
        "PPSEN": 0.249,
        "EM-FL": 17.4,
        "FL-SH": 6.0,
        "FL-SD": 13.5,
        "SD-PM": 32.4,
        "FL-LF": 26.0,
        "LFMAX": 1.03,
        "SLAVR": 375.0,
        "SIZLF": 180.0,
        "XFRT": 1.0,
        "WTPSD": 0.19,
        "SFDUR": 23.0,
        "SDPDV": 2.2,
        "PODUR": 10.0,
        "THRSH": 77.0,
        "SDPRO": 0.405,
        "SDLIP": 0.205,
    },

    # Wheat
    "WH NEWTON (Chelsea soft white)" : {
        "@VAR#": "IB0488",
        "EXP#": "1,6",
        "ECO#": "USWH01",
        "P1V": 48.45,
        "P1D": 73.5,
        "P5": 505.0,
        "G1": 35.42,
        "G2": 22.6,
        "G3": 0.78,
        "PHINT": 95.0,
    }

}

CROP_NAMES_TO_CROP_MODELS = {
    "Maize": "MZCER48", # TO-DO: change this to MZIXM48 after PRing to DSSATTools
    "Soybean": "CRGRO48",
    "Wheat": "WHCER48",
}

MINIMUM_REQUIRED_FARMER_INPUTS = ["crop_name", "crop_variety", "latitude", "longitude", "elevation", 
                           "planting_date", "is_irrigation_applied", "irrigation_application"]


# OUTPUT_CODE_TYPES_FROM_DSSATTOOLS = ['PlantGro', "Weather", "SoilWat", "SoilOrg"]
OUTPUT_CODE_TYPES_FROM_DSSATTOOLS = ['PlantGro', "Weather", "SoilWat"]

CDE_SUFIX_SEP = "__"

SUMMARY_OUT_CATEGORIES_COLS = {
    "IDENTIFIERS": ['RUNNO', 'TRNO', 'R#', 'O#', 'P#', 'CR', 'MODEL'],
    "EXPERIMENT AND TREATMENT": ['EXNAME', 'TNAM'],
    "SITE INFORMATION": ['FNAM', 'WSTA', 'WYEAR', 'SOIL_ID', 'LAT', 'LONG', 'ELEV'],
    "DATES": ['SDAT', 'PDAT', 'EDAT', 'ADAT', 'MDAT', 'HDAT',  'HYEAR'],
    "DRY WEIGHT, YIELD AND YIELD COMPONENTS": ['DWAP', 'CWAM', 'HWAM', 'HWAH', 'BWAH', 'PWAM', 'HWUM', 'H#AM', 'H#UM', 'HIAM', 'LAIX'],
    "FRESH WEIGHT": ["FCWAM", "FHWAM", "HWAHF", "FBWAH", "FPWAM"],
    "WATER": ['IR#M', 'IRCM', 'PRCM', 'ETCM', 'EPCM', 'ESCM', 'ROCM', 'DRCM', 'SWXM'],
    "NITROGEN": ['NI#M', 'NICM', 'NFXM', 'NUCM', 'NLCM', 'NIAM', 'CNAM', 'GNAM', 'N2OEM'],
    "PHOSPHORUS": ['PI#M', 'PICM', 'PUPC', 'SPAM'],
    "POTASSIUM": ['KI#M', 'KICM', 'KUPC', 'SKAM'],
    "ORGANIC MATTER": ['RECM', 'ONTAM', 'ONAM', 'OPTAM', 'OPAM', 'OCTAM', 'OCAM', 'CO2EM', 'CH4EM'],
    "WATER PRODUCTIVITY": ['DMPPM', 'DMPEM', 'DMPTM', 'DMPIM', 'YPPM', 'YPEM', 'YPTM', 'YPIM'],
    "NITROGEN PRODUCTIVITY": ['DPNAM', 'DPNUM', 'YPNAM', 'YPNUM'],
    "SEASONAL ENVIRONMENTAL DATA (Planting to harvest)": ['NDCH', 'TMAXA', 'TMINA', 'SRADA', 'DAYLA', 'CO2A', 'PRCP', 'ETCP', 'ESCP', 'EPCP'],
    "STATUS": ['CRST'],
}

ASSUMPTIONS = {

    # the below were taken from Dr. Rasu's SQX model and their associated files. see `references/` folder
    "fertilizer_material_code": "IB001",
    "fertilizer_application_code": DSSAT_NA_VALUE,
    "fertilizer_depth": 10,
    "fertilizer_Ca": 0,
    "fertilizer_other_elements_applied": 0, # Other elements in applied fertilizer
    "fertilizer_other_elements_code": DSSAT_NA_VALUE, # Other element code, e.g.,. MG
    "fertilizer_name": DSSAT_NA_VALUE,
    "avg_annual_soil_temperature": 9.2, # also see https://github.com/eusojk/dssatsim/issues/1
    "amplitude_soil_temperature": 13.0, # also see https://github.com/eusojk/dssatsim/issues/2

    # for the below, see: https://github.com/daquinterop/Py_DSSATTools/blob/29da1eea7d2bf2d03a2be7c4534aef7e5798bcca/DSSATTools/management.py#L91
    "simulation_start": None,   # will be calculated as previous day to the planting date
    "emergence_date": None,     # will be calculated as 5 days after planting
    "initial_swc": 1,           # Fraction of the total available water set to 100%
    "harvest_management_option": "M",        # set to `At Maturity`
    "organic_matter_management_option": "G", # Ceres (Godiwn)

    # Other assumptions/default/constants
    "irrigation_operation_code": "IR001",

}
