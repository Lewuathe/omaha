from cachetools import cached
from dateutil import parser
import pandas as pd
import quandl

from omaha.joinable import Joinable

class Company(Joinable):
    def __init__(self, ticker, from_q, to_q, client):
        self.ticker = ticker
        self.client = client
        self.from_q = from_q
        self.to_q = to_q
        super().__init__([self])

    @classmethod
    def dict_pairs(cls, d, keys):
        return {k:v for k, v in d.items() if k in keys}

    @cached(cache={})
    def __get(self, from_q, to_q):
        return self.client.quarter(self.ticker, from_q, to_q)

    def get(self, item):
        res = self.__get(self.from_q, self.to_q)
        keys = [item, 'fiscal_year', 'fiscal_quarter']
        return [Company.dict_pairs(d, keys) for d in res[self.ticker]]

    def all(self):
        res = self.__get(self.from_q, self.to_q)
        return res[self.ticker]

    def raw_df(self):
        res = self.__get(self.from_q, self.to_q)
        df = pd.DataFrame(res[self.ticker])
        index = [pd.Timestamp(s, tz='UTC') for s in df['end_date']]
        df.index = index
        return df

class Stockprice(Joinable):
    def __init__(self, ticker, start_date, end_date):
        self.ticker = ticker
        self.start_date = start_date
        self.end_date = end_date
        super().__init__([self])

    def raw_df(self):
        df = quandl.get(f'XJPX/{self.ticker}0', start_date=self.start_date, end_date=self.end_date)
        df.index = [pd.Timestamp(s, tz='UTC') for s in df.index]
        return df
