import pandas as pd

class Joinable(object):
    def __init__(self, joinables):
        self.joinables = joinables

    def join(self, other):
        return Joinable(self.joinables + other.joinables)

    def raw_df(self):
        pass

    def df(self):
        dfs = [j.raw_df() for j in self.joinables]
        return pd.concat(dfs, axis=1, join='inner')
