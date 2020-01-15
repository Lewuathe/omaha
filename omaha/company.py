from cachetools import cached
from dateutil import parser
import pandas as pd
import quandl

from omaha.joinable import Joinable


class Company(Joinable):
    """Container for the financial indicators of the public company

    Attributes:
        ticker (str): Ticker symbol
        from_q (str): Beginning quarter of the target range
        to_q (str): End quarter of the target range
        client (Client): BuffettCode API Client
    """
    def __init__(self, ticker, from_q, to_q, client):
        self.ticker = ticker
        self.client = client
        self.from_q = from_q
        self.to_q = to_q
        super().__init__([self])

    @classmethod
    def dict_pairs(cls, d, keys):
        return {k: v for k, v in d.items() if k in keys}

    @cached(cache={})
    def __get(self, from_q, to_q):
        return self.client.quarter(self.ticker, from_q, to_q)

    def __str__(self):
        return f"Company({self.ticker}, {self.from_q}, {self.to_q})"

    def __repr__(self):
        return self.__str__()

    def get(self, item):
        res = self.__get(self.from_q, self.to_q)
        keys = [item, "fiscal_year", "fiscal_quarter"]
        return [Company.dict_pairs(d, keys) for d in res[self.ticker]]

    def all(self):
        res = self.__get(self.from_q, self.to_q)
        return res[self.ticker]

    def raw_df(self):
        res = self.__get(self.from_q, self.to_q)
        df = pd.DataFrame(res[self.ticker])
        index = [pd.Timestamp(s, tz="UTC") for s in df["end_date"]]
        df.index = index
        return df


class Stockprice(Joinable):
    """Container for the daily stockprice of the public company.
    """
    def __init__(self, ticker, start_date, end_date):
        self.ticker = ticker
        self.start_date = start_date
        self.end_date = end_date
        super().__init__([self])

    def raw_df(self):
        df = quandl.get(
            f"XJPX/{self.ticker}0", start_date=self.start_date, end_date=self.end_date
        )
        df.index = [pd.Timestamp(s, tz="UTC") for s in df.index]
        return df
