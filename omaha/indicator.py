import pandas as pd
from cachetools import cached

from .client import Client


class Indicator(object):
    """
    Financial indicators for the given company
    """

    def __init__(self, apikey):
        self.client = Client(apikey=apikey)

    @cached(cache={})
    def get(self, ticker, from_q, to_q):
        q = self.client.quarter(ticker, from_q, to_q)
        # c = self.client.company(ticker)
        return pd.DataFrame(q[ticker])
