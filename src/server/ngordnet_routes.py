from server.ngordnet_views import index
from server.ngordnet_handler import QueryHandler 

def setup_routes(app):
    app.router.add_get('/', index)