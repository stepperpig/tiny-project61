from collections import defaultdict
from ngrams.timeseries import TimeSeries
import pandas as pd

class NGramMap():

    MAP = defaultdict(list)
    COUNTS = defaultdict(float)

    # yeah lets just make this as unreadable as possible why not
    def __init__(self, wfile, cfile):
        self.wfile = wfile 
        self.cfile = cfile 

    def _parse_words(self, wfile):
        words_df = pd.read_csv(wfile, sep='\t', header=None, 
                               usecols=[0,1,2], names=['word', 'year', 'appearances'])
        # we have to iterate through this entire dataframe and 
        # insert into MAP

        return 
        
    def _parse_counts(self, cfile):
        return
