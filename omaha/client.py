import pandas as pd
import requests
import json


class Client(object):
    """
    Buffett Code API Client
    """

    ENDPOINT = "https://api.buffett-code.com"

    def _get(self, path, params = {}):
        headers = {"x-api-key": self.apikey}
        return requests.get(
            f"{Client.ENDPOINT}/api/v2{path}", params=params, headers=headers
        )

    def __init__(self, apikey):
        self.apikey = apikey

    def quarter(self, ticker, from_q, to_q):
        res = self._get("/quarter", {"tickers": ticker, "from": from_q, "to": to_q})
        j = res.json()
        return j

    def company(self, ticker):
        res = self._get("/company")
        j = res.json()
        return j[ticker]

    def search(self, keywords):
        res = self._get("/search", {"keywords": keywords})
        j = res.json()
        return j
