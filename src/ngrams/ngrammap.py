from collections import defaultdict
from ngrams.timeseries import TimeSeries
import pandas as pd


def custom_func(x):
    year_list = x['year'].tolist()
    count_list = x['appearances'].tolist()
    ts = TimeSeries()
    for i in range(len(year_list)):
        ts.put(year_list[i], count_list[i])
    return ts

class NGramMap():

    MAP = defaultdict(TimeSeries)     # we'll adapt this to store TimeSeries
    COUNTS = defaultdict(float)

    # yeah lets just make this as unreadable as possible why not
    def __init__(self, wfile, cfile):
        self._parse_words(wfile)
        self._parse_counts(cfile)

    
    def _parse_words(self, wfile):
        words_df = pd.read_csv(wfile, sep='\t', header=None, 
                               usecols=[0,1,2], names=['word', 'year', 'appearances'])

        g = words_df.groupby('word', group_keys=False).apply(custom_func, include_groups=False).to_dict()
        self.MAP = g
        
    def _parse_counts(self, cfile):
        counts_df = pd.read_csv(cfile, sep=',', header=None,
                                usecols=[0,1], names=['year', 'total'], 
                                dtype={'year': 'int16', 'total': 'float32'})
        n = len(counts_df['year'])
        for i in range(n):
            year = int(counts_df['year'][i])
            total = float(counts_df['total'][i])
            self.COUNTS[year] = total

    def countHistory(self, *args):
        if len(args) == 1:
            ts = TimeSeries()
            if self.MAP.get(args[0]) is None:
                return ts
            ts = self.MAP.get(args[0])
            return ts
        else:
            ts = TimeSeries()
            if self.MAP.get(args[0]) is None:
                return ts
            ts = self.MAP.get(args[0])
            bounded_ts = TimeSeries(ts, args[1], args[2])
            return bounded_ts
    
    def totalCountHistory(self):
        ts = TimeSeries()
        for k, v in self.COUNTS:
            ts.put(k, v)
        return ts
    
    def weightHistory(self, *args):
        if len(args) == 1:
            ts = TimeSeries()
            ts2 = self.totalCountHistory()
            if self.MAP.get(args[0]) is None:
                return ts
            else:
                ts = self.countHistory(args[0])
                return ts.dividedBy(ts2)
        else:
            ts = TimeSeries()
            ts2 = self.totalCountHistory()
            if self.MAP.get(args[0]) is None:
                return ts
            else:
                ts = self.countHistory(args[0], args[1], args[2])
                bounded_ts2 = TimeSeries(ts2, args[1], args[2])
                return ts.dividedBy(bounded_ts2)
            
    def summedWeightHistory(self, *args):
        if len(args) == 1:
            sum = TimeSeries()
            for word in args[0]:
                if len(self.countHistory(word)) == 0:
                    continue
                if len(sum) == 0:
                    sum = self.countHistory(word)
                else:
                    ts = self.countHistory(word)
                    sum = sum.plus(ts)
            total = self.totalCountHistory()
            return sum.dividedBy(total)
        else:
            sum = TimeSeries()
            for word in args[0]:
                if len(self.countHistory(word, args[1], args[2])) == 0:
                    continue
                if len(sum) == 0:
                    sum = self.countHistory(word, args[1], args[2])
                else:
                    ts = self.countHistory(word, args[1], args[2])
                    sum = sum.plus(ts)
            total = TimeSeries(self.totalCountHistory(), args[1], args[2])
            return sum.dividedBy(total)

    def print(self):
        print(self.MAP)

    def words(self):
        # get all keys of the dict
        return self.MAP.keys()

    def histories(self):
        return self.MAP.values()
