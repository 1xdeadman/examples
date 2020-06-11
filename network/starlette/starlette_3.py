from starlette.applications import Starlette
from starlette.responses import PlainTextResponse, JSONResponse
from starlette.routing import Route, Mount


async def homepage(request):
    app.state.ADMIN_EMAIL = 'admin@example.org'
    return PlainTextResponse("Homepage")


async def about(request):
    text = "About: "
    text += app.state.ADMIN_EMAIL  # может быть краш!
    return PlainTextResponse(text)


async def user(req):
    username = req.path_params['username']
    return PlainTextResponse(f"hello, {username}")


async def kek(req):
    return JSONResponse(f"kek")


async def horde(req):
    return PlainTextResponse(f"ты прав!")


async def aliance(req):
    username = req.path_params['username']
    return JSONResponse(f"Сам ты, {username}, сосед!")


routes = [
    Route("/", endpoint=homepage),
    Route("/about", endpoint=about),
    Route('/users/{username}', user),  # localhost:8000/users/23c23c
    Route('/kek', kek, methods=["POST"]),
    
    Mount('/lol', routes=[
        Route('/ordasosed', horde),  # localhost:8000/lol/ordasosed
        Route('/alyanssosed/{username}', aliance)  # localhost:8000/lol/alyanssosed/123
    ])
]

app = Starlette(routes=routes)