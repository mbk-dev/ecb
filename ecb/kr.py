import pandas as pd
import ecb


def get_main_rate() -> pd.Series:
    s = ecb.request_data.get_data_frame("FM", "D.U2.EUR.4F.KR.MRR_FR.LEV")
    s.rename("main_rate", inplace=True)
    return s / 100


def get_deposit_rate() -> pd.Series:
    s = ecb.request_data.get_data_frame("FM", "D.U2.EUR.4F.KR.DFR.LEV")
    s.rename("deposit_rate", inplace=True)
    return s / 100


def get_marginal_rate(
    start_period: str = "1900-01-01", end_period: str = None
) -> pd.Series:
    s = ecb.request_data.get_data_frame(
        "FM",
        "D.U2.EUR.4F.KR.MLFR.LEV",
        start_period=start_period,
        end_period=end_period,
    )
    s.rename("marginal_rate", inplace=True)
    return s / 100
