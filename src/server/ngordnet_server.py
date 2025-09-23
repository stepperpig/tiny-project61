from aiohttp import web
import aiohttp_cors
from aiohttp.web_request import Request
from aiohttp.web_response import Response
from server.ngordnet_routes import setup_routes

# routes = web.RouteTableDef()

class Server():
    def __init__(self):
        self.app = web.Application()
        # setup_routes(self.app)
        # self.app.router.add_static('/static', path='./static')
        # self.app.router.add_get('/historytext')

    def start(self):
        web.run_app(self.app, port=4567)
