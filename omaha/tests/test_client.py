import unittest
import requests_mock

from omaha.client import Client


class ClientTest(unittest.TestCase):
    def setUp(self):
        self.client = Client(apikey="apikey")

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
            r = self.client.quarter("1111", "2019Q1", "2019Q4")
            self.assertEqual(len(r["1111"]), 1)
