import pandas
from redblacktree.rbtree import RBTree 

# We need to implement a Red-Black-Tree to replicate
# a TreeMap.
class TimeSeries(RBTree):
    min_year = 1400
    max_year = 2100

    def __init__(self):
        super().__init__()

    def __init__(self, ts, startYear, endYear):
        super().__init__()
        if startYear > endYear:
            raise ValueError("Can't be greater than a year that doesn't exist!")
        else:
            for 

    def years(self):
        years = [] 
        for year in self.keySet():
            years.append(year)
        return years
