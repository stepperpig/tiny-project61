import unittest
import math
from ngrams.timeseries import TimeSeries
from ngrams.ngrammap import NGramMap

class NGramMapTest(unittest.TestCase):
    
    def testCountHistory(self):
        short_words_file = "/Users/kaiwenli/Documents/projects/skeleton-sp24/data/ngrams/very_short.csv"
        total_counts_file = "/Users/kaiwenli/Documents/projects/skeleton-sp24/data/ngrams/total_counts.csv"
        ngm = NGramMap(short_words_file, total_counts_file)

        expectedYears = [2005, 2006, 2007, 2008]
        expectedCounts = [646179.0, 677820.0, 697645.0, 795265.0]

        request2005to2008 = ngm.countHistory("request")
        self.assertEqual(request2005to2008.years(), expectedYears)

if __name__ == "__main__":
    unittest.main()