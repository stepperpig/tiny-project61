from aiohttp import web
from aiohttp.web_request import Request
from aiohttp.web_response import Response

from datetime import datetime
routes = web.RouteTableDef()

class Server():

    def __init__(self):
        self.app = web.Application()
        self.app.add_routes(routes)

    # handle the get request
    def register(self, url, nqh):
        return 
        

    def start(self):
        web.run_app(self.app)

    # TEST_DUMMY: create endpoint for getting time
    @routes.get('/time')
    async def time(request: Request) -> Response:
        today = datetime.today()
        result = {
            'month': today.month,
            'day': today.day,
            'time': str(today.time())
        }
        return web.json_response(result)
