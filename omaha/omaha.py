from .client import Client
from .company import Company
from .company import Stockprice
import quandl

class Omaha(object):
    """Omaha provides a unified view of the financial information of the public companies."""

    def __init__(self, bc_apikey, quandl_apikey):
        self.client = Client(bc_apikey)
        quandl.ApiConfig.api_key = quandl_apikey

    def company(self, ticker, from_q, to_q):
        """Basic financial indicators of the company

        :param ticker: str
        :param from_q: str
        :param to_q: str
        :return: Company
        :rtype: Company

        :Example:
        >>>
        """
        return Company(ticker, from_q, to_q,  self.client)

    def stockprice(self, ticker, start_date, end_date):
        """Stockprice of the given company
        """
        return Stockprice(ticker, start_date, end_date)

    def search(self, keywords, from_q, to_q):
        """List of matched companies
        """
        tickers = self.client.search(keywords)
        return [self.company(ticker, from_q, to_q) for ticker in tickers]
