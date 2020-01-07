import pandas as pd
from cachetools import cached

class Company(object):
    def __init__(self, ticker, client):
        self.ticker = ticker
        self.client = client

    @classmethod
    def dict_pairs(cls, d, keys):
        return {k:v for k, v in d.items() if k in keys}

    @cached(cache={})
    def __get(self, from_q, to_q):
        return self.client.quarter(self.ticker, from_q, to_q)

    def get(self, item, from_q, to_q):
        res = self.__get(from_q, to_q)
        keys = [item, 'fiscal_year', 'fiscal_quarter']
        return [Company.dict_pairs(d, keys) for d in res[self.ticker]]

    def all(self, from_q, to_q):
        res = self.__get(from_q, to_q)
        return res[self.ticker]

    def df(self, from_q, to_q):
        res = self.__get(from_q, to_q)
        return pd.DataFrame(res[self.ticker])
