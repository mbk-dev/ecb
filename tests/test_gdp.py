import pandas as pd
import pytest

from ecb.gdp import get_gdp_q

SAMPLE_CSV_GDP = (
    "KEY,FREQ,REF_AREA,ADJUSTMENT,ACTIVITY,STS_INSTITUTION,STS_CONCEPT,STS_SUFFIX,TIME_PERIOD,OBS_VALUE\n"
    "MNA.Q.N.I8.W2.S1.S1.B.B1GQ._Z._Z._Z.EUR.V.N,Q,I8,N,B1GQ,S1,B,V,2024-Q1,3200000.0\n"
    "MNA.Q.N.I8.W2.S1.S1.B.B1GQ._Z._Z._Z.EUR.V.N,Q,I8,N,B1GQ,S1,B,V,2024-Q2,3250000.0\n"
)


@pytest.fixture()
def mock_ecb_api(requests_mock):
    from ecb.request_data import URL_BASE

    requests_mock.get(URL_BASE + "MNA/Q.N.I8.W2.S1.S1.B.B1GQ._Z._Z._Z.EUR.V.N", text=SAMPLE_CSV_GDP)


class TestGetGdpQ:
    def test_returns_series(self, mock_ecb_api):
        result = get_gdp_q()
        assert isinstance(result, pd.Series)

    def test_name(self, mock_ecb_api):
        result = get_gdp_q()
        assert result.name == "gdp"

    def test_quarterly_period_index(self, mock_ecb_api):
        result = get_gdp_q()
        assert isinstance(result.index, pd.PeriodIndex)
        assert result.index.freqstr == "Q-DEC"

    def test_values(self, mock_ecb_api):
        result = get_gdp_q()
        assert result.iloc[0] == pytest.approx(3200000.0)
        assert result.iloc[1] == pytest.approx(3250000.0)

    def test_length(self, mock_ecb_api):
        result = get_gdp_q()
        assert len(result) == 2

    def test_with_date_range(self, mock_ecb_api):
        result = get_gdp_q(start_period="2024-01-01", end_period="2024-06-30")
        assert isinstance(result, pd.Series)
