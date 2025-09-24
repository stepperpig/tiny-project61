import pandas
import math
from typing import overload
from redblacktree.rbtree import RedBlackMap

# We need to implement a Red-Black-Tree to replicate
# a TreeMap.
class TimeSeries(RedBlackMap):
    min_year = 1400
    max_year = 2100

    def __init__(self, *args):
        if len(args) == 0:
            super().__init__()
        else:
            super().__init__()
            ts = args[0]
            startYear = args[1]
            endYear = args[2]
            if startYear > endYear:
                raise ValueError("something went wrong")
            else:
                for key in ts:
                    if (startYear <= key) and (key <= endYear):
                        x = ts.get(key)
                        self.put(key, x)

    def years(self):
        years = [] 
        for year in self:
            years.append(year)
        return years

    def data(self):
        data = []
        for key in self:
            x = self.get(key)
            data.append(x)
        return data
    
    def plus(self, ts):
        sum = TimeSeries()
        if len(self.years()) == 0 and len(ts.years()) == 0:
            return sum
        startYear = min(self.firstKey(), ts.firstKey())
        endYear = max(self.lastKey(), ts.lastKey())

        i = startYear
        while i <= endYear:
            if self.get(i) is None:
                if ts.get(i):
                    tmp = ts.get(i)
                    sum.put(i, tmp)
                else:
                    i += 1
                    continue 
            else:
                if ts.get(i) is None:
                    tmp = self.get(i)
                    sum.put(i, tmp)
                else:
                    tmp1 = self.get(i)
                    tmp2 = ts.get(i)
                    sum.put(i, tmp1 + tmp2)
            i += 1
        return sum

    def dividedBy(self, ts):
        quotient = TimeSeries()
        if len(self.years()) == 0 and len(ts.years()) == 0:
            return quotient
        startYear = min(self.firstKey(), ts.firstKey())
        endYear = max(self.lastKey(), ts.lastKey())

        i = startYear
        while i <= endYear:
            if self.get(i) is None:
                if ts.get(i):
                    i += 1
                    continue
            else:
                if ts.get(i) is None:
                    raise ValueError("invalid value")
                else:
                    tmp1 = self.get(i)
                    tmp2 = ts.get(i)
                    quotient.put(i, tmp1 / tmp2)
            i += 1
        return quotient