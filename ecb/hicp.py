import pandas as pd
import ecb
from datetime import date

today = date.today()


def get_hicp(start_period: str = "1900-01-01", end_period: str = None) -> pd.Series:
    s = ecb.request_data.get_data_frame(
        "ICP",
        "M.U2.N.000000.4.INX",
        "M",
        start_period=start_period,
        end_period=end_period,
    )
    s.rename("HICP", inplace=True)
    return s
