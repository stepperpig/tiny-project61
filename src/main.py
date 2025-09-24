from aiohttp import web
import aiohttp_cors
import json
from ngrams.ngrammap import NGramMap 
from server.ngordnet_server import Server
from server.ngordnet_routes import setup_routes

def main():
    wfile = "/Users/kaiwenli/Documents/projects/skeleton-sp24/data/ngrams/very_short.csv"
    cfile = "/Users/kaiwenli/Documents/projects/skeleton-sp24/data/ngrams/total_counts.csv"
    map = NGramMap(wfile, cfile)

    server = Server()
    setup_routes(server.app) 
    server.start()

main()