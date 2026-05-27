import pandas as pd
import pytest

from ecb.hicp import get_hicp

SAMPLE_CSV_HICP = (
    "KEY,FREQ,REF_AREA,UNIT,COICOP,STS_SUFFIX,TIME_PERIOD,OBS_VALUE\n"
    "ICP.M.U2.N.000000.4.INX,M,U2,N,000000,INX,2024-01,118.32\n"
    "ICP.M.U2.N.000000.4.INX,M,U2,N,000000,INX,2024-02,118.68\n"
    "ICP.M.U2.N.000000.4.INX,M,U2,N,000000,INX,2024-03,119.15\n"
)


@pytest.fixture()
def mock_ecb_api(requests_mock):
    from ecb.request_data import URL_BASE

    requests_mock.get(URL_BASE + "ICP/M.U2.N.000000.4.INX", text=SAMPLE_CSV_HICP)


class TestGetHicp:
    def test_returns_series(self, mock_ecb_api):
        result = get_hicp()
        assert isinstance(result, pd.Series)

    def test_name(self, mock_ecb_api):
        result = get_hicp()
        assert result.name == "HICP"

    def test_monthly_period_index(self, mock_ecb_api):
        result = get_hicp()
        assert isinstance(result.index, pd.PeriodIndex)
        assert result.index.freqstr == "M"

    def test_values(self, mock_ecb_api):
        result = get_hicp()
        assert result.iloc[0] == pytest.approx(118.32)
        assert result.iloc[-1] == pytest.approx(119.15)

    def test_length(self, mock_ecb_api):
        result = get_hicp()
        assert len(result) == 3

    def test_with_date_range(self, mock_ecb_api):
        result = get_hicp(start_period="2024-01-01", end_period="2024-03-31")
        assert isinstance(result, pd.Series)
