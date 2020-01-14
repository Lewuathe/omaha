import unittest
from unittest.mock import MagicMock
import requests_mock

from omaha.company import Company
from omaha.client import Client


class CompanyTest(unittest.TestCase):
    def setUp(self):
        mock_client = Client(apikey="xxx")
        mock_client.quarter = MagicMock(
            return_value={
                "column_description": {
                    "company_name": {"name_jp": "会社名", "unit": "なし"}
                },
                "1111": [
                    {
                        "company_name": "海山商事",
                        "fiscal_year": "2019",
                        "fiscal_quarter": "4",
                    },
                    {
                        "company_name": "海山商事",
                        "fiscal_year": "2019",
                        "fiscal_quarter": "3",
                    },
                ],
            }
        )
        self.company = Company("1111", "2019Q1", "2019Q4", mock_client)

    def test_dict_pairs(self):
        res = Company.dict_pairs({"a": 1, "b": 2, "c": 3}, ["a", "b"])
        self.assertEqual({"a": 1, "b": 2}, res)

    def test_company_name(self):
        expected = [
            {"company_name": "海山商事", "fiscal_quarter": "4", "fiscal_year": "2019"},
            {"company_name": "海山商事", "fiscal_quarter": "3", "fiscal_year": "2019"},
        ]
        self.assertEqual(expected, self.company.get("company_name"))
