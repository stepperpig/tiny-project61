from aiohttp import web

class QueryHandler:
    def __init__(self):
        pass

    def serve(self, filename):
        return web.FileResponse('./static/ngordnet_2a.html')

    def _strtolist(self, s):
        requested_words = s.split(',')
        return requested_words

    async def handle(self, request):
        data = await request.get()
        s = data.get('words')
        words = self._strtolist(s)
        startYear = data.get('startYear')
        endYear = data.get('endYear')
        return web.Response(text=startYear)