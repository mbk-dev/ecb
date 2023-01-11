import pandas as pd
import ecb


def get_refinancing_rate(start_date: pd.Timestamp = pd.Timestamp(1900, 1, 1),
                         end_date:pd.Timestamp = None) -> pd.Series:
    """
    Get ECB main refinancing operations key rate monthly time series.
    """
    start_period = start_date.strftime("%Y-%m-%d")
    if end_date != None:
        end_period = end_date.strftime("%Y-%m-%d")
    else:
        end_period = None
    s = ecb.request_data.get_data_frame("FM", "D.U2.EUR.4F.KR.MRR_FR.LEV",
                                        start_period=start_period, end_period=end_period)
    s.rename("main_rate", inplace=True)
    return s / 100


def get_deposit_rate(start_date: pd.Timestamp = pd.Timestamp(1900, 1, 1),
                         end_date:pd.Timestamp = None) -> pd.Series:
    """
    Get ECB key rate on the deposit facility monthly time series.

    On deposit facility rate banks can make overnight deposits with the Eurosystem.
    """
    start_period = start_date.strftime("%Y-%m-%d")
    if end_date != None:
        end_period = end_date.strftime("%Y-%m-%d")
    else:
        end_period = None
    s = ecb.request_data.get_data_frame("FM", "D.U2.EUR.4F.KR.DFR.LEV",
                                        start_period=start_period, end_period=end_period)
    s.rename("deposit_rate", inplace=True)
    return s / 100


def get_marginal_rate(start_date: pd.Timestamp = pd.Timestamp(1900, 1, 1),
                         end_date:pd.Timestamp = None) -> pd.Series:
    """
    Get ECB key rate on marginal lending facility monthly time seriesю

    On marginal lending facility rate ECB may offer overnight credit to banks from the Eurosystem.
    """

    start_period = start_date.strftime("%Y-%m-%d")
    if end_date != None:
        end_period = end_date.strftime("%Y-%m-%d")
    else:
        end_period = None
    s = ecb.request_data.get_data_frame(
        "FM",
        "D.U2.EUR.4F.KR.MLFR.LEV",
        start_period=start_period,
        end_period=end_period
    )
    s.rename("marginal_rate", inplace=True)
    return s / 100
