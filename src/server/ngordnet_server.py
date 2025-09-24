from aiohttp import web
import json
import aiohttp_cors
from aiohttp.web_request import Request
from aiohttp.web_response import Response
from server.ngordnet_handler import QueryHandler
from pathlib import Path
import os

from pathlib import Path

class Server():
    def __init__(self):
        self.app = web.Application()

    def register(self, handler):
        self.app.router.add_get('/historytext', handler._handle_history_text)

    def setup_routes(self): 
        root = Path(__file__).parent.parent
        # self.app.router.add_get('/historytext', _handle_history_text)
        self.app.add_routes([web.static('/', os.path.join(root, 'static/'), show_index=True)])
        self.app.router.add_get('/', self._serve_index)
        self._set_cors()

    def _set_cors(self):
        # set CORS for all routes in list
        # set CORS policy
        cors = aiohttp_cors.setup(self.app, defaults={
            "*": aiohttp_cors.ResourceOptions(
                allow_credentials=True,
                expose_headers="*",
                allow_headers="*",
                allow_methods=["GET", "POST", "PUT", "DELETE"]
            )
        })
        for route in list(self.app.router.routes()):
            cors.add(route)

    async def _serve_index(self, request):
        return web.HTTPFound('/static/ngordnet_2a.html')

    def start(self):
        web.run_app(self.app, host='localhost', port=4567)
