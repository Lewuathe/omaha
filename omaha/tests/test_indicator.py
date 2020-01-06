import unittest
import requests_mock

from omaha.indicator import Indicator


class IndicatorTest(unittest.TestCase):
    def setUp(self):
        self.indicator = Indicator(apikey="apikey")

    def test_quarter(self):
        with requests_mock.Mocker() as m:
            response = {
                "1111": [{"company_name": "海山商事"}],
                "column_description": {
                    "company_name": {"name_jp": "会社名", "unit": "なし"}
                },
            }
            m.get(
                "https://api.buffett-code.com/api/v2/quarter?tickers=1111&from=2019Q1&to=2019Q4",
                json=response,
            )
            df = self.indicator.get("1111", "2019Q1", "2019Q4")
            self.assertEqual(df.columns, ["company_name"])
