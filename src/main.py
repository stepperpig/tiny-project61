from aiohttp import web
import aiohttp_cors
import json
from ngrams.ngrammap import NGramMap 
from server.ngordnet_server import Server

def main():
    # wfile = "/Users/kaiwenli/Documents/projects/skeleton-sp24/data/ngrams/words_that_start_with_q.csv"
    # cfile = "/Users/kaiwenli/Documents/projects/skeleton-sp24/data/ngrams/total_counts.csv"
    # map = NGramMap(wfile, cfile)

    # user tries to retrieve unigram history data. they input a list of words. we handle
    # this input on the backend through our handler, which is supposed to return a plot of the
    # correct timeseries. for now we'll just send that data in the form of text.
    server = Server()
    server.app.router.add_get('/historytext', get_data)
    # server.app.router.add_static('/static', path='./static')
    cors = aiohttp_cors.setup(server.app, defaults={
        "*": aiohttp_cors.ResourceOptions(
            allow_credentials=True,
            expose_headers="*",
            allow_headers="*",
            allow_methods=["GET", "POST", "PUT", "DELETE"]
        )
    })
    for route in list(server.app.router.routes()):
        cors.add(route)
    server.start()

async def get_data(request):
    request_data = {
        "url": str(request.url),
    }
    serialized_request = json.dumps(request_data)
    print(serialized_request)
    return web.Response(text="OK")

main()