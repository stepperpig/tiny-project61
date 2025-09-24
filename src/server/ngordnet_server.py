from aiohttp import web
import json
import aiohttp_cors
from aiohttp.web_request import Request
from aiohttp.web_response import Response
import os
from pathlib import Path

class Server():
    def __init__(self):
        self.app = web.Application()
        # root = self._get_project_root()

        # self.app.router.add_get('/historytext', self._handle_history_text)
        # self.app.add_routes([web.static('/', os.path.join(root, 'static/'), show_index=True)])
        # self.app.router.add_get('/', self._serve_index)

        # # set CORS policy
        # cors = aiohttp_cors.setup(self.app, defaults={
        #     "*": aiohttp_cors.ResourceOptions(
        #         allow_credentials=True,
        #         expose_headers="*",
        #         allow_headers="*",
        #         allow_methods=["GET", "POST", "PUT", "DELETE"]
        #     )
        # })
        # # set CORS for all routes in list
        # for route in list(self.app.router.routes()):
        #     cors.add(route)

    # helper to find project root
    # def _get_project_root(self) -> Path:
    #     return Path(__file__).parent.parent
    
    # async def _handle_history_text(self, request):
    #     # get words
    #     word_str = request.query.get('words')
    #     word_list = word_str.split(',')
    #     # get start and end years
    #     startYear_returned = request.query.get('startYear')
    #     startYear = int(startYear_returned)
    #     endYear_returned = request.query.get('endYear')
    #     endYear = int(endYear_returned)
    #     # load into json object
    #     json_obj = {
    #         "words": word_list,
    #         "startYear": int(startYear),
    #         "endYear": int(endYear)
    #     }
    #     return web.json_response(json_obj)

    # async def _serve_index(self, request):
        # return web.HTTPFound('/static/ngordnet_2a.html')

    def start(self):
        web.run_app(self.app, host='localhost', port=4567)
