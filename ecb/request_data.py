import pandas as pd
import requests
from io import StringIO

from requests import Response

URL_BASE = "https://sdw-wsrest.ecb.europa.eu/service/data/"
URL_END = "/"


def get_data_frame(agency: str = 'FM', code: str = 'D.U2.EUR.4F.KR.MRR_FR.LEV', freq: str = 'D',
                   detail: str = "dataonly", format: str = "csvdata",
                   startperiod: str = '1900-01-01', endperiod: str = None) -> pd.Series:
    request_url = URL_BASE + agency + URL_END + code
    params = {'detail': detail,
              'format': format,
              'startPeriod': startperiod,
              'endPeriod': endperiod
              }
    try:
        abc: Response = requests.get(request_url, params=params)
    except requests.exceptions.HTTPError as err:
        raise requests.exceptions.HTTPError(
            f"HTTP error fetching data for {code}:",
            abc.status_code,
            abc.reason,
            URL_BASE,
        ) from err
    jresp = abc.text
    df = pd.read_csv(StringIO(jresp),
                     usecols=['TIME_PERIOD', 'OBS_VALUE'],
                     dtype={'OBS_VALUE': float},
                     parse_dates=['TIME_PERIOD'])
    df.rename(columns={df.columns[0]: "date"}, inplace=True)
    df.set_index('date', inplace=True)
    df.index = df.index.to_period(freq=freq)
    return df.squeeze()
