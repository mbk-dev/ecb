import pandas as pd
import requests
from io import StringIO

from requests import Response

URL_begin = "https://sdw-wsrest.ecb.europa.eu/service/data/"
URL_end = "/"


def get_data_frame(agency: str = 'FM', code: str = 'D.U2.EUR.4F.KR.MRR_FR.LEV', freq: str = 'D',
                   detail: str = "dataonly", format: str = "csvdata",
                   startperiod: str = '1900-01-01', endperiod: str = None) -> pd.Series:
    request_url = URL_begin + agency + URL_end + code
    params = {'detail': detail,
              'format': format,
              'startPeriod': startperiod,
              'endPeriod': endperiod
              }
    abc: Response = requests.get(request_url, params=params)
    jresp = abc.text
    df = pd.read_csv(StringIO(jresp),
                     usecols=['TIME_PERIOD', 'OBS_VALUE'],
                     dtype={'OBS_VALUE': float},
                     parse_dates=['TIME_PERIOD'])
    df.set_index('TIME_PERIOD', inplace=True)
    df.index = df.index.to_period(freq=freq)
    return df
