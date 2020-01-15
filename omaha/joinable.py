import pandas as pd


class Joinable(object):
    """Joinable views

    The dataframe of the class can be joined with the end date of the financial report.
    """

    def __init__(self, joinables):
        self.joinables = joinables

    def join(self, other):
        """Joined with other financial data container.
        """
        return Joinable(self.joinables + other.joinables)

    def raw_df(self):
        pass

    def df(self):
        """DataFrame representing the underlying financial data.

        Returns:
            DataFrame: DataFrame representing the underlying financial data
        """
        dfs = [j.raw_df() for j in self.joinables]
        return pd.concat(dfs, axis=1, join="inner")
