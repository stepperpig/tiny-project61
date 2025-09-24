from server.ngordnet_views import index
from server.ngordnet_handler import QueryHandler 
from aiohttp import web
import os
import aiohttp_cors
from pathlib import Path

def setup_routes(app):
    root = _get_project_root()
    app.router.add_get('/historytext', _handle_history_text)
    app.add_routes([web.static('/', os.path.join(root, 'static/'), show_index=True)])
    app.router.add_get('/', _serve_index)
    _set_cors(app)

# helper to find project root
def _get_project_root() -> Path:
    return Path(__file__).parent.parent

def _set_cors(app):
    # set CORS for all routes in list
    # set CORS policy
    cors = aiohttp_cors.setup(app, defaults={
        "*": aiohttp_cors.ResourceOptions(
            allow_credentials=True,
            expose_headers="*",
            allow_headers="*",
            allow_methods=["GET", "POST", "PUT", "DELETE"]
        )
    })
    for route in list(app.router.routes()):
        cors.add(route)

async def _handle_history_text(request):
    # get words
    word_str = request.query.get('words')
    word_list = word_str.split(',')
    # get start and end years
    startYear_returned = request.query.get('startYear')
    startYear = int(startYear_returned)
    endYear_returned = request.query.get('endYear')
    endYear = int(endYear_returned)
    # load into json object
    json_obj = {
        "words": word_list,
        "startYear": int(startYear),
        "endYear": int(endYear)
    }
    return web.json_response(json_obj)

async def _serve_index(request):
    return web.HTTPFound('/static/ngordnet_2a.html')