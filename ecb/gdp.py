import pandas as pd
import ecb


def get_gdp_q(start_period: str = "1900-01-01", end_period: str = None) -> pd.Series:
    s = ecb.request_data.get_data_frame(
        agency="MNA",
        code="Q.N.I8.W2.S1.S1.B.B1GQ._Z._Z._Z.EUR.V.N",
        freq="Q",
        start_period=start_period,
        end_period=end_period,
    )
    s.rename("gdp", inplace=True)
    return s
