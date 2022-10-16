import pandas as pd
import ecb
def get_main_rate() -> pd.Series:
    df = ecb.request_data.get_data_frame('FM', 'D.U2.EUR.4F.KR.MRR_FR.LEV')
    return df

def get_deposit_rate() -> pd.Series:
    df = ecb.request_data.get_data_frame('FM', 'D.U2.EUR.4F.KR.DFR.LEV')
    return df

def get_marginal_rate() -> pd.Series:
    df = ecb.request_data.get_data_frame('FM', 'D.U2.EUR.4F.KR.MLFR.LEV')
    return df

