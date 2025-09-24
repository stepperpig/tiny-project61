from aiohttp import web
import aiohttp_cors
import json
from ngrams.ngrammap import NGramMap 
from server.ngordnet_server import Server
from server.ngordnet_handler import QueryHandler

def main():
    wfile = "/Users/kaiwenli/Documents/projects/skeleton-sp24/data/ngrams/very_short.csv"
    cfile = "/Users/kaiwenli/Documents/projects/skeleton-sp24/data/ngrams/total_counts.csv"

    # alternate user
    wf = "/Users/I764248/Downloads/data/ngrams/very_short.csv"
    cf = "/Users/I764248/Downloads/data/ngrams/total_counts.csv"


    map = NGramMap(wfile, cfile)

    server = Server()
    handler = QueryHandler(map)
    server.register(handler)
    server.setup_routes()
    server.start()

main()