import unittest
from unittest.mock import MagicMock
import requests_mock

from omaha.company import Company
from omaha.client import Client


class JoinableTest(unittest.TestCase):
    def setUp(self):
        mock_client1 = Client(apikey="xxx")
        mock_client1.quarter = MagicMock(
            return_value={
                "column_description": {
                    "company_name": {"name_jp": "会社名", "unit": "なし"}
                },
                "1111": [
                    {
                        "end_date": "2019-01-01",
                        "company_name": "海山商事",
                        "fiscal_year": "2019",
                        "fiscal_quarter": "4",
                    },
                    {
                        "end_date": "2019-01-02",
                        "company_name": "海山商事",
                        "fiscal_year": "2019",
                        "fiscal_quarter": "3",
                    },
                ],
            }
        )
        self.company1 = Company("1111", "2019Q1", "2019Q4", mock_client1)
        mock_client2 = Client(apikey="xxx")
        mock_client2.quarter = MagicMock(
            return_value={
                "column_description": {
                    "company_name": {"name_jp": "会社名", "unit": "なし"}
                },
                "2222": [
                    {
                        "end_date": "2019-01-01",
                        "company_name": "海山商事",
                        "fiscal_year": "2019",
                        "fiscal_quarter": "4",
                    },
                    {
                        "end_date": "2019-01-03",
                        "company_name": "海山商事",
                        "fiscal_year": "2019",
                        "fiscal_quarter": "3",
                    },
                ],
            }
        )
        self.company2 = Company("2222", "2019Q1", "2019Q4", mock_client2)

    def test_join(self):
        joined = self.company1.join(self.company2)
        df = joined.df()
        self.assertEqual(8, df.size)
        self.assertEqual(1, df.index.size)
