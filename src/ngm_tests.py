import unittest
import math
from ngrams.timeseries import TimeSeries
from ngrams.ngrammap import NGramMap

class NGramMapTest(unittest.TestCase):
    
    def testCountHistory(self):
        short_words_file = "/Users/kaiwenli/Documents/projects/skeleton-sp24/data/ngrams/very_short.csv"
        total_counts_file = "/Users/kaiwenli/Documents/projects/skeleton-sp24/data/ngrams/total_counts.csv"

        # alternate user
        wf = "/Users/I764248/Downloads/data/ngrams/very_short.csv"
        cf = "/Users/I764248/Downloads/data/ngrams/total_counts.csv"

        ngm = NGramMap(short_words_file, total_counts_file)

        expectedYears = [2005, 2006, 2007, 2008]
        expectedCounts = [646179.0, 677820.0, 697645.0, 795265.0]

        request2005to2008 = ngm.countHistory("request")
        self.assertEqual(request2005to2008.years(), expectedYears)

        for i in range(len(expectedCounts)):
            self.assertTrue(math.isclose( request2005to2008.data()[i], expectedCounts[i], rel_tol=1e-10 ))


        expectedYears = [2006, 2007]
        expectedCounts = [677820.0, 697645.0]
        
        request2006to2007 = ngm.countHistory("request", 2006, 2007)
        self.assertEqual(request2006to2007.years(), expectedYears)

        for i in range(len(expectedCounts)):
            self.assertTrue(math.isclose( request2006to2007.data()[i], expectedCounts[i], rel_tol=1e-10 ))

    def testOnLargeFile(self):
        top_14337_words_file = "/Users/kaiwenli/Documents/projects/skeleton-sp24/data/ngrams/top_14377_words.csv"
        total_counts_file = "/Users/kaiwenli/Documents/projects/skeleton-sp24/data/ngrams/total_counts.csv"

        wf = "/Users/I764248/Downloads/data/ngrams/top_14377_words.csv"
        cf = "/Users/I764248/Downloads/data/ngrams/total_counts.csv"

        ngm = NGramMap(top_14337_words_file, total_counts_file)

        fishCount = ngm.countHistory("fish", 1850, 1933)
        self.assertTrue(math.isclose(fishCount.get(1865), 136497.0, rel_tol=1e-10))
        self.assertTrue(math.isclose(fishCount.get(1922), 444924.0, rel_tol=1e-10))


if __name__ == "__main__":
    suite = unittest.TestSuite()
    suite.addTest(NGramMapTest('testOnLargeFile'))
    runner = unittest.TextTestRunner()
    runner.run(suite)