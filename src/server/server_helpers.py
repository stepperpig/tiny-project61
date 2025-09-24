from pathlib import Path
import aiohttp_cors

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