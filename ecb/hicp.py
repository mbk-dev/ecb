import pandas as pd
import ecb
from datetime import date

today = date.today()


def get_hicp(startperiod: str = '1900-01-01', endperiod: str = None) -> pd.Series:
    s = ecb.request_data.get_data_frame("ICP", "M.U2.N.000000.4.INX", "M",
                                        startperiod=startperiod, endperiod=endperiod)
    s.rename("HICP", inplace=True)
    return s
