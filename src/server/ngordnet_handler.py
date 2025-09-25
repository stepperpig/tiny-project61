from aiohttp import web
from ngrams.ngrammap import NGramMap
from collections import defaultdict
from ngrams.timeseries import TimeSeries

class QueryHandler:
    m = defaultdict(TimeSeries)
    def __init__(self, ngm):
        self.m = ngm

    async def _handle_history_text(self, request):
        # get words
        word_str = request.query.get('words')
        word_list = word_str.split(',')
        # get start and end years
        startYear_returned = request.query.get('startYear')
        startYear = int(startYear_returned)
        endYear_returned = request.query.get('endYear')
        endYear = int(endYear_returned)
        # load into json object
        json_obj = {
            "words": word_list,
            "startYear": int(startYear),
            "endYear": int(endYear)
        }
        # we need to return a timeseries here. in d3, a line chart
        # requires a JSON object with a date and a floating-point
        # value. that's fine, but we'll be using a multiline chart
        # to visualize multiple timeseries. we'll just need a specific
        # word and a year.
        # we have to send back a flat array of objects. for each of our
        # words, we'll construct a countHistory timeseries. 
        # we'll parse every year into a JSON object.
        
        timeseries = []
        for word in word_list:
            ts = self.m.countHistory(word)
            bounded_ts = TimeSeries(ts, startYear, endYear)
            timeseries.append((word, bounded_ts))


        j_obj = []
        for t in timeseries:
            w, s = t
            for y in s.years():
                obj = {"word": w, "year": y, "count": s.get(y)}
                j_obj.append(obj)

        return web.json_response(j_obj)