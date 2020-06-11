from starlette.applications import Starlette
from starlette.responses import PlainTextResponse, JSONResponse, HTMLResponse
from starlette.routing import Route, Mount
import starlette.middleware as middleware


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
    Route('/users/{username}', user),
    Route('/kek', kek, methods=["POST"]),
    Mount('/lol', routes=[
        Route('/ordasosed', horde),
        Route('/alyanssosed/{username}', aliance)
    ])
]


HTML_404_PAGE = "not found"
HTML_500_PAGE = "server error"


async def not_found(request, exc):
    return HTMLResponse(content=HTML_404_PAGE, status_code=exc.status_code)


async def server_error(request, exc):
    return HTMLResponse(content=HTML_500_PAGE, status_code=exc.status_code)



class my_middleware(BaseHTTPMiddleware):
    async def dispatch(self, req, call_next):
        response = await call_next(req)
        response.headers['my_header'] = 'my_middleware'



exception_handlers = {
    404: not_found,
    500: server_error
}


middleware_list = [
    middleware.Middleware(middleware.errors.ServerErrorMiddleware),
    middleware.Middleware(my_middleware)
]

app = Starlette(routes=routes, exception_handlers=exception_handlers, middleware=middleware_list)
