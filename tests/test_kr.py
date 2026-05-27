import pandas as pd
import pytest

from ecb.kr import get_deposit_rate, get_marginal_rate, get_refinancing_rate

SAMPLE_CSV_RATE = (
    "KEY,FREQ,REF_AREA,CURRENCY,PROVIDER_FM,INSTRUMENT_FM,PROVIDER_FM_ID,DATA_TYPE_FM,TIME_PERIOD,OBS_VALUE\n"
    "FM.D.U2.EUR.4F.KR.MRR_FR.LEV,D,U2,EUR,4F,KR,MRR_FR,LEV,2024-01-02,4.5\n"
    "FM.D.U2.EUR.4F.KR.MRR_FR.LEV,D,U2,EUR,4F,KR,MRR_FR,LEV,2024-01-03,4.25\n"
)


@pytest.fixture()
def mock_ecb_api(requests_mock):
    def _mock(url_pattern="FM/", csv_text=SAMPLE_CSV_RATE):
        from ecb.request_data import URL_BASE

        requests_mock.get(URL_BASE + url_pattern, text=csv_text)

    return _mock


class TestGetRefinancingRate:
    def test_returns_series(self, mock_ecb_api):
        mock_ecb_api("FM/D.U2.EUR.4F.KR.MRR_FR.LEV")
        result = get_refinancing_rate()
        assert isinstance(result, pd.Series)

    def test_name(self, mock_ecb_api):
        mock_ecb_api("FM/D.U2.EUR.4F.KR.MRR_FR.LEV")
        result = get_refinancing_rate()
        assert result.name == "main_rate"

    def test_values_divided_by_100(self, mock_ecb_api):
        mock_ecb_api("FM/D.U2.EUR.4F.KR.MRR_FR.LEV")
        result = get_refinancing_rate()
        assert result.iloc[0] == pytest.approx(0.045)
        assert result.iloc[1] == pytest.approx(0.0425)

    def test_period_index(self, mock_ecb_api):
        mock_ecb_api("FM/D.U2.EUR.4F.KR.MRR_FR.LEV")
        result = get_refinancing_rate()
        assert isinstance(result.index, pd.PeriodIndex)

    def test_with_date_range(self, mock_ecb_api):
        mock_ecb_api("FM/D.U2.EUR.4F.KR.MRR_FR.LEV")
        start = pd.Timestamp(2024, 1, 1)
        end = pd.Timestamp(2024, 1, 31)
        result = get_refinancing_rate(start_date=start, end_date=end)
        assert isinstance(result, pd.Series)


class TestGetDepositRate:
    def test_returns_series(self, mock_ecb_api):
        mock_ecb_api("FM/D.U2.EUR.4F.KR.DFR.LEV")
        result = get_deposit_rate()
        assert isinstance(result, pd.Series)

    def test_name(self, mock_ecb_api):
        mock_ecb_api("FM/D.U2.EUR.4F.KR.DFR.LEV")
        result = get_deposit_rate()
        assert result.name == "deposit_rate"

    def test_values_divided_by_100(self, mock_ecb_api):
        mock_ecb_api("FM/D.U2.EUR.4F.KR.DFR.LEV")
        result = get_deposit_rate()
        assert result.iloc[0] == pytest.approx(0.045)

    def test_with_date_range(self, mock_ecb_api):
        mock_ecb_api("FM/D.U2.EUR.4F.KR.DFR.LEV")
        start = pd.Timestamp(2024, 1, 1)
        end = pd.Timestamp(2024, 1, 31)
        result = get_deposit_rate(start_date=start, end_date=end)
        assert isinstance(result, pd.Series)


class TestGetMarginalRate:
    def test_returns_series(self, mock_ecb_api):
        mock_ecb_api("FM/D.U2.EUR.4F.KR.MLFR.LEV")
        result = get_marginal_rate()
        assert isinstance(result, pd.Series)

    def test_name(self, mock_ecb_api):
        mock_ecb_api("FM/D.U2.EUR.4F.KR.MLFR.LEV")
        result = get_marginal_rate()
        assert result.name == "marginal_rate"

    def test_values_divided_by_100(self, mock_ecb_api):
        mock_ecb_api("FM/D.U2.EUR.4F.KR.MLFR.LEV")
        result = get_marginal_rate()
        assert result.iloc[0] == pytest.approx(0.045)

    def test_with_date_range(self, mock_ecb_api):
        mock_ecb_api("FM/D.U2.EUR.4F.KR.MLFR.LEV")
        start = pd.Timestamp(2024, 1, 1)
        end = pd.Timestamp(2024, 1, 31)
        result = get_marginal_rate(start_date=start, end_date=end)
        assert isinstance(result, pd.Series)
