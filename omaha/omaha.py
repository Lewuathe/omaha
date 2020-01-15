from .client import Client
from .company import Company
from .company import Stockprice
import quandl


class Omaha(object):
    """Omaha provides a unified view of the financial information of the public companies.

    Attributes:
        bc_apikey (str): Apikey of BuffettCode API
        quandl_apikey (str): Apikey of Quandl
    """

    def __init__(self, bc_apikey, quandl_apikey):
        self.client = Client(bc_apikey)
        quandl.ApiConfig.api_key = quandl_apikey

    def company(self, ticker, from_q, to_q):
        """Basic financial indicators of the company

        Args:
            ticker (str): Ticker symbol
            from_q (str): Beginning of the target quarter
            to_q (str): End of the target quarter

        Returns:
            Company: Target company

        Example:
            >>> factory = Omaha(bc_apikey='xxxx'), quandl_apikey='yyyy')
            >>> factory.company('1111', '2019Q1', '2019Q4')
        """
        return Company(ticker, from_q, to_q, self.client)

    def stockprice(self, ticker, start_date, end_date):
        """Stockprice of the given company

        Args:
            ticker (str): Ticker symbol
            start_date (str): Start date of the target range
            end_date (str): End date of the target range

        Returns:
            Stockprice: Object containing stock prices

        Example:
            >>> factory = Omaha(bc_apikey='xxxx'), quandl_apikey='yyyy')
            >>> factory.stockprice('1111', '2019-01-01', '2019-12-31')
        """
        return Stockprice(ticker, start_date, end_date)

    def search(self, keywords, from_q, to_q):
        """List of matched companies with given search keyword

        Args:
            keywords (str): Keyword used for searching companies
            from_q (str): Beginning quarter of the target range
            to_q (str): End quarter of the target range

        Returns:
          list: List of companies matching with the given keyword.

        Example:
            >>> factory = Omaha(bc_apikey='xxxx'), quandl_apikey='yyyy')
            >>> factory.search('不動産', '2019-01-01', '2019-12-31')
        """
        tickers = self.client.search(keywords)
        return [self.company(ticker, from_q, to_q) for ticker in tickers]

    def category(self, cat, from_q, to_q):
        """List of companies filtering by the given TSE 33 sectors.

        See: https://www.jpx.co.jp/english/markets/indices/line-up/files/e_fac_13_sector.pdf

        Args:
            keywords (str): Keyword used for searching companies
            from_q (str): Beginning quarter of the target range
            to_q (str): End quarter of the target range

        Returns:
          list: List of companies matching with the given TSE 33 sectors.

        Example:
            >>> factory = Omaha(bc_apikey='xxxx'), quandl_apikey='yyyy')
            >>> factory.category('サービス業', '2019-01-01', '2019-12-31')
        """
        companies = self.client.companies()
        tickers = []
        for ticker, company in companies.items():
            if ticker == 'column_description':
                continue
            if company[0]['tosyo_33category'] == cat:
                tickers.append(ticker)

        return [self.company(ticker, from_q, to_q) for ticker in tickers]


