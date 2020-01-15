.. omaha documentation master file, created by
   sphinx-quickstart on Tue Jan 14 11:53:07 2020.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Omaha
=================================

.. image:: https://img.shields.io/pypi/v/omaha
.. image:: https://img.shields.io/pypi/pyversions/omaha
.. image:: https://img.shields.io/pypi/l/omaha
.. image:: https://img.shields.io/pypi/dd/omaha

------------------------------------------------------------------
Unified view of financial metrics of public companies
------------------------------------------------------------------

Omaha aims to provide a unified view of financial metrics of the company. It's designed to provide comprehensive data set for the financial analysis.

- Combining multiple type of financial data consistently.
- Data is provided in Pandas DataFrame format for the usability.

.. code:: python

   from omaha import Omaha

   factory = Omaha(bc_apikey='XXXXXXX', quandl_apikey='YYYYYYY')

   # Financial indicators for the ticker symbol 1376
   company = factory.company('1376', '2018Q1', '2019Q4')

   # Daily stock prices for the ticker symbol 1376
   stockprice = factory.stockprice('1376', '2018-01-01', '2018-12-31')

   # Joining multiple indicators
   view = company.join(stockprice)
   view.df().head()

   #                             company_name     ceo_name                  headquarters_address        ...   Low         Close
   #2018-11-30 00:00:00+00:00    カネコ種苗株式会社  代表取締役社長　　金子　昌彦   群馬県前橋市古市町一丁目50番地12 ...  1389.568777  1408.187823
   #2018-08-31 00:00:00+00:00    カネコ種苗株式会社  代表取締役社長　　金子　昌彦   群馬県前橋市古市町一丁目50番地12 ...  1479.188532  1479.188532

   factory.search("不動産", "2019Q1", "2019Q4")
   # [Company(8881, 2019Q1, 2019Q4), Company(8802, 2019Q1, 2019Q4), Company(3465, 2019Q1, 2019Q4),...]

-----------------------
How to install
-----------------------

.. toctree::
   :maxdepth: 2

   how_to_install

---------------------------------
External Services
---------------------------------

Omaha is dependent on the external services to get the fresh financial data. This is the list of services used in omaha.

- `Buffett Code <https://www.buffett-code.com/>`_
- `Quandl <https://www.quandl.com/>`_

Please get the API keys for these service in advance.

---------------------------------
API Documentation
---------------------------------

.. toctree::
   :maxdepth: 2

   omaha