import unittest
from typing import overload
from ngrams.timeseries import TimeSeries

class TimeSeriesTest(unittest.TestCase):
    def test_from_spec(self):
        catPopulation = TimeSeries()
        catPopulation.put(1991, 0.0)
        catPopulation.put(1992, 100.0)
        catPopulation.put(1994, 200.0)

        dogPopulation = TimeSeries()
        dogPopulation.put(1994, 400.0)
        dogPopulation.put(1995, 500.0)

        expectedYears = [1991, 1992, 1994]
        self.assertEqual(catPopulation.years(), expectedYears)

    def test_populated_ts(self):
        bigcatPopulation = TimeSeries()
        bigcatPopulation.put(1991, 0.0)
        bigcatPopulation.put(1992, 100.0)
        bigcatPopulation.put(1994, 200.0)
        bigcatPopulation.put(1995, 100.0)
        bigcatPopulation.put(1996, 300.0)

        newBigCatPopulation = TimeSeries(bigcatPopulation, 1992, 1995)

        expectedYears = [1992, 1994, 1995]
        self.assertEqual(newBigCatPopulation.years(), expectedYears)

if __name__ == "__main__":
    unittest.main()