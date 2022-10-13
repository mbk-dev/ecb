import pandas as pd
import ecb
def get_mrr_fr() -> pd.Series:
    dcsv = ecb.request_data.get_data_frame()
    df = pd.Series()
    return df

def get_dfr() -> pd.Series:
    df = pd.Series()
    return df
