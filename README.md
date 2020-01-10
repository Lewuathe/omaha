# Omaha

Omaha aims to provide a unified view of financial metrics of the company.

- Designed to provide comprehensive data set for the financial analysis.
- Combining multiple type of financial data consistently.
- Data is provided in Pandas DataFrame format for the usability.

## Note

It only supports Japanese company for now.

## Dependencies

- [Buffett Code](https://www.buffett-code.com)
- [Quandl](https://www.quandl.com/)

## Install

```
$ pip install omaha
```

## Usage

```python
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
```

## Development

You can develop the package as editable dependencies with Pipenv.

```
$ pipenv install --dev -e .
```

To build the package, run `make package`.

```
$ make package
```
