import pandas as pd
import requests
import json
from cachetools import cached

class Client(object):
    """
    Buffett Code API Client

    Attributes:
        apikey (str): Apikey for BuffettCode API
    """

    ENDPOINT = "https://api.buffett-code.com"

    def _get(self, path, params={}):
        headers = {"x-api-key": self.apikey}
        return requests.get(
            f"{Client.ENDPOINT}/api/v2{path}", params=params, headers=headers
        )

    def __init__(self, apikey):
        self.apikey = apikey

    @cached(cache={})
    def quarter(self, ticker, from_q, to_q):
        """Quarter endpoint

        See: http://docs.buffett-code.com/#/default/get_api_v2_quarter

        Parameters:
          ticker (str): Ticker symbol
          from_q (str): Beginning quarter of the target range
          to_q (str): End quarter of the target range

        """
        res = self._get("/quarter", {"tickers": ticker, "from": from_q, "to": to_q})
        j = res.json()
        return j

    @cached(cache={})
    def companies(self):
        """Company endpoint

        See: http://docs.buffett-code.com/#/default/get_api_v2_company
        """
        res = self._get("/company")
        j = res.json()
        return j

    @cached(cache={})
    def search(self, keywords):
        """Search endpoint

        See: http://docs.buffett-code.com/#/default/get_api_v2_search
        """
        res = self._get("/search", {"keywords": keywords})
        j = res.json()
        return j
