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

        self.app.add_routes([web.static('/static', os.path.join(root, 'static'))])
        self.app.add_routes([web.get('', self._get_data)])

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

    async def _get_data(self, request):
        request_data = {
            "url": str(request.url),
        }
        serialized_request = json.dumps(request_data)
        print(serialized_request)
        return web.Response()

    def _get_project_root(self) -> Path:
        return Path(__file__).parent.parent

    def start(self):
        web.run_app(self.app, port=4567)
