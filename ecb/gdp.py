import pandas as pd
import ecb


def get_gdp_q(startperiod: str = '1900-01-01', endperiod: str = None) -> pd.Series:
    s = ecb.request_data.get_data_frame(agency='MNA',code='Q.N.I8.W2.S1.S1.B.B1GQ._Z._Z._Z.EUR.V.N',
                                       freq='Q', startperiod=startperiod, endperiod=endperiod)
    s.rename("GBP", inplace=True)
    return s
