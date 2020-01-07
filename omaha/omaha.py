from .client import Client
from .company import Company

class Omaha(object):
    def __init__(self, apikey):
        self.apikey = apikey
        self.client = Client(self.apikey)

    def company(self, ticker):
        return Company(ticker, self.client)