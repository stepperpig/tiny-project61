from collections import defaultdict
from ngrams.timeseries import TimeSeries
import pandas as pd

class NGramMap():

    MAP = defaultdict(list)     # we'll adapt this to store TimeSeries
    COUNTS = defaultdict(float)

    # yeah lets just make this as unreadable as possible why not
    def __init__(self, wfile, cfile):
        self._parse_words(wfile)
        self._parse_counts(cfile)

    def _parse_words(self, wfile):
        words_df = pd.read_csv(wfile, sep='\t', header=None, 
                               usecols=[0,1,2], names=['word', 'year', 'appearances'])
        # we have to iterate through this entire dataframe and 
        # insert into MAP
        n = len(words_df['word'])
        for i in range(n):
            self.MAP[words_df['word'][i]].append((words_df['year'][i], words_df['appearances'][i]))
        
    def _parse_counts(self, cfile):
        counts_df = pd.read_csv(cfile, sep=',', header=None,
                                usecols=[0,1], names=['year', 'total'], 
                                dtype={'year': 'int16', 'total': 'float32'})
        n = len(counts_df['year'])
        for i in range(n):
            self.COUNTS[counts_df['year'][i]] = counts_df['total'][i]

    def print(self):
        print(self.MAP)

    def words(self):
        # get all keys of the dict
        return self.MAP.keys()

    def histories(self):
        return self.MAP.values()
