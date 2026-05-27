import pandas as pd
import pytest
import requests

from ecb.request_data import URL_BASE, get_data_frame

SAMPLE_CSV = (
    "KEY,FREQ,REF_AREA,CURRENCY,PROVIDER_FM,INSTRUMENT_FM,PROVIDER_FM_ID,DATA_TYPE_FM,TIME_PERIOD,OBS_VALUE\n"
    "FM.D.U2.EUR.4F.KR.MRR_FR.LEV,D,U2,EUR,4F,KR,MRR_FR,LEV,2024-01-02,4.5\n"
    "FM.D.U2.EUR.4F.KR.MRR_FR.LEV,D,U2,EUR,4F,KR,MRR_FR,LEV,2024-01-03,4.5\n"
    "FM.D.U2.EUR.4F.KR.MRR_FR.LEV,D,U2,EUR,4F,KR,MRR_FR,LEV,2024-01-04,4.25\n"
)

SAMPLE_CSV_QUARTERLY = (
    "KEY,FREQ,REF_AREA,ADJUSTMENT,ACTIVITY,STS_INSTITUTION,STS_CONCEPT,STS_SUFFIX,TIME_PERIOD,OBS_VALUE\n"
    "MNA.Q.N.I8.W2.S1.S1.B.B1GQ._Z._Z._Z.EUR.V.N,Q,I8,N,B1GQ,S1,B,V,2024-Q1,3200000.0\n"
    "MNA.Q.N.I8.W2.S1.S1.B.B1GQ._Z._Z._Z.EUR.V.N,Q,I8,N,B1GQ,S1,B,V,2024-Q2,3250000.0\n"
)


class TestURLBase:
    def test_uses_new_ecb_endpoint(self):
        assert "data-api.ecb.europa.eu" in URL_BASE

    def test_url_base_ends_with_slash(self):
        assert URL_BASE.endswith("/")


class TestGetDataFrame:
    def test_returns_series(self, requests_mock):
        requests_mock.get(URL_BASE + "FM/D.U2.EUR.4F.KR.MRR_FR.LEV", text=SAMPLE_CSV)
        result = get_data_frame("FM", "D.U2.EUR.4F.KR.MRR_FR.LEV", start_period="2024-01-01", end_period="2024-01-04")
        assert isinstance(result, pd.Series)

    def test_series_values(self, requests_mock):
        requests_mock.get(URL_BASE + "FM/D.U2.EUR.4F.KR.MRR_FR.LEV", text=SAMPLE_CSV)
        result = get_data_frame("FM", "D.U2.EUR.4F.KR.MRR_FR.LEV")
        assert result.iloc[0] == 4.5
        assert result.iloc[-1] == 4.25

    def test_daily_period_index(self, requests_mock):
        requests_mock.get(URL_BASE + "FM/D.U2.EUR.4F.KR.MRR_FR.LEV", text=SAMPLE_CSV)
        result = get_data_frame("FM", "D.U2.EUR.4F.KR.MRR_FR.LEV", freq="D")
        assert isinstance(result.index, pd.PeriodIndex)
        assert result.index.freqstr == "D"

    def test_quarterly_period_index(self, requests_mock):
        requests_mock.get(URL_BASE + "MNA/Q.N.I8.W2.S1.S1.B.B1GQ._Z._Z._Z.EUR.V.N", text=SAMPLE_CSV_QUARTERLY)
        result = get_data_frame("MNA", "Q.N.I8.W2.S1.S1.B.B1GQ._Z._Z._Z.EUR.V.N", freq="Q")
        assert isinstance(result.index, pd.PeriodIndex)
        assert result.index.freqstr == "Q-DEC"

    def test_length_matches_csv_rows(self, requests_mock):
        requests_mock.get(URL_BASE + "FM/D.U2.EUR.4F.KR.MRR_FR.LEV", text=SAMPLE_CSV)
        result = get_data_frame("FM", "D.U2.EUR.4F.KR.MRR_FR.LEV")
        assert len(result) == 3

    def test_passes_query_params(self, requests_mock):
        requests_mock.get(URL_BASE + "FM/D.U2.EUR.4F.KR.MRR_FR.LEV", text=SAMPLE_CSV)
        get_data_frame("FM", "D.U2.EUR.4F.KR.MRR_FR.LEV", start_period="2024-01-01", end_period="2024-01-31")
        assert requests_mock.called
        qs = requests_mock.last_request.qs
        assert qs["startperiod"] == ["2024-01-01"]
        assert qs["endperiod"] == ["2024-01-31"]
        assert qs["format"] == ["csvdata"]
        assert qs["detail"] == ["dataonly"]
