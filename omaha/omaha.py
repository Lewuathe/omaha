from .client import Client
from .company import Company
from .company import Stockprice
import quandl

class Omaha(object):
    def __init__(self, bc_apikey, quandl_apikey):
        self.client = Client(bc_apikey)
        quandl.ApiConfig.api_key = quandl_apikey

    def company(self, ticker, from_q, to_q):
        return Company(ticker, from_q, to_q,  self.client)

    def stockprice(self, ticker, start_date, end_date):
        return Stockprice(ticker, start_date, end_date)