from aiohttp import web
import json
import aiohttp_cors
from aiohttp.web_request import Request
from aiohttp.web_response import Response
from server.ngordnet_routes import setup_routes
import os
from pathlib import Path

# routes = web.RouteTableDef()

class Server():
    def __init__(self):
        self.app = web.Application()
        root = self._get_project_root()

        self.app.router.add_get('/historytext', self._handle_history_text)
        self.app.add_routes([web.static('/', os.path.join(root, 'static/'), show_index=True)])
        self.app.router.add_get('/', self._serve_index)

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

    def _get_project_root(self) -> Path:
        return Path(__file__).parent.parent
    
    async def _handle_history_text(self, request):
        word_str = request.query.get('words')
        word_list = word_str.split(',')

        startYear = request.query.get('startYear')
        endYear = request.query.get('endYear')
        return web.json_response({'words': word_list, 'startYear': int(startYear), 'endYear': int(endYear)},
                                 status=200)

    async def _serve_index(self, request):
        return web.HTTPFound('/static/ngordnet_2a.html')

    def start(self):
        web.run_app(self.app, host='localhost', port=4567)
