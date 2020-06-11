# инфа про http: https://developer.mozilla.org/ru/docs/Web/HTTP/Overview
# оф. документация: https://www.starlette.io/
# оф репозиторий проекта: https://github.com/encode/starlette
# информация об ассинхронных серверах: https://habr.com/ru/post/482936/
# https://asgi.readthedocs.io/en/latest/
# https://www.uvicorn.org/
# Django
# Flask
# AioHTTP
# Sanic
# Tornado
# starlette

# pip install starlette
# pip install uvicorn

# uvicorn starlette_1:app

from starlette.applications import Starlette
from starlette.responses import JSONResponse
from starlette.routing import Route


async def homepage(request):
    return JSONResponse({'hello': 'world'})


async def req_1(request):
    return JSONResponse({'kek': 'lol'})

my_routes = [
    Route('/', homepage),
    Route('/request', req_1),
]


app = Starlette(debug=False, routes=my_routes)