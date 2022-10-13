import pandas as pd
import ecb
def get_main_rate() -> pd.Series:
    df = ecb.request_data.get_data_frame('MRR_FR')
    return df

def get_deposit_rate() -> pd.Series:
    df = ecb.request_data.get_data_frame('DFR')
    return df

def get_marginal_rate() -> pd.Series:
    df = ecb.request_data.get_data_frame('MLFR')
    return df

