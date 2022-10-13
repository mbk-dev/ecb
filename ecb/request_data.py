import pandas as pd
import requests
from io import StringIO

from requests import Response

URL_begin = "https://sdw-wsrest.ecb.europa.eu/service/data/FM/D.U2.EUR.4F.KR."
URL_end = ".LEV"
def get_data_frame(code: str = 'MRR_FR', detail: str = "dataonly", format: str = "csvdata") -> pd.Series:
    request_url = URL_begin + code + URL_end
    params = {'detail': detail,
              'format': format
              }
    abc: Response = requests.get(request_url, params=params)
    jresp = abc.text
    df = pd.read_csv(StringIO(jresp),
                     usecols=['TIME_PERIOD','OBS_VALUE'],
                     dtype={'OBS_VALUE': float},
                     parse_dates=['TIME_PERIOD'])
    df.set_index('TIME_PERIOD', inplace=True)
    df.index = df.index.to_period(freq='D')
    return df