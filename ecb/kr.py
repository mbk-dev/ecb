import pandas as pd
import ecb
def get_main_rate() -> pd.Series:
    return ecb.request_data.get_data_frame('MRR_FR')

def get_deposit_rate() -> pd.Series:
    return ecb.request_data.get_data_frame('DFR')

def get_marginal_rate() -> pd.Series:
    return ecb.request_data.get_data_frame('MLFR')

