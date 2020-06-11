# pip install starlette-jwt
# pip install cryptography - RS256
from starlette.applications import Starlette
from starlette_jwt import JWTAuthenticationBackend
from starlette.middleware.authentication import AuthenticationMiddleware
from starlette.authentication import requires
from starlette.responses import JSONResponse


app = Starlette()

'''
def my_handler(request):
    @app.route('/noauth')
    @requires('authenticated')
    async def homepage(request):
        return JSONResponse({'payload': request.session})
'''

@app.route('/noauth')
async def homepage(request):
    return JSONResponse({'payload': None})


@app.route('/auth')
@requires('authenticated')
async def auth_homepage(request):
    return JSONResponse({'payload': request.headers['Authorization']})

with open('E:\\certs\\jwtRS256.key.pub', 'rb') as jwt_file:
    public_key = jwt_file.read()
print(public_key)
# public_key = b'-----BEGIN PUBLIC KEY-----\nMHYwEAYHKoZIzj0CAQYFK4EEAC...'
app.add_middleware(AuthenticationMiddleware, backend=JWTAuthenticationBackend(secret_key=public_key, prefix='Bearer', algorithm='RS256', username_field='user'))