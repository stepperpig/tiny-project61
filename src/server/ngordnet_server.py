from aiohttp import web
from aiohttp.web_request import Request
from aiohttp.web_response import Response
from server.ngordnet_routes import setup_routes

from datetime import datetime
routes = web.RouteTableDef()

class Server():
    def __init__(self):
        self.app = web.Application()
        setup_routes(self.app)
        # self.app.router.add_static('/static', path='./static')

    def start(self):
        web.run_app(self.app)
