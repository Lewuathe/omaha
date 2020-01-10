# Omaha

Omaha aims to provide a unified view of financial metrics of the company.

- Designed to provide comprehensive data set for the financial analysis.
- Combining multiple type of financial data consistently.

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
stockprice = factory.stockprice('1376')
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
