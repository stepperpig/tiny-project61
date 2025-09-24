from aiohttp import web
from ngrams.ngrammap import NGramMap
from collections import defaultdict
from ngrams.timeseries import TimeSeries

class QueryHandler:
    def __init__(self, ngm):
        pass

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
        return web.json_response(json_obj)