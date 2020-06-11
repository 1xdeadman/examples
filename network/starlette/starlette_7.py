# pip install motor
# https://docs.mongodb.com/drivers/motor
# https://motor.readthedocs.io/en/stable/
# https://motor.readthedocs.io/en/stable/tutorial-asyncio.html
import datetime


from starlette.applications import Starlette
from starlette.responses import JSONResponse
from starlette.routing import Route

import motor
import motor.motor_asyncio


import config

def connect():
    app.state.client = motor.motor_asyncio.AsyncIOMotorClient('localhost', 27017)
    app.state.db = app.state.client['Test']


async def find(request):
    try:
        username = request.path_params['username']
        collection = app.state.db['history']
        res = await collection.find_one({'user': username})
        if res is not None:
            date = res['date'].strftime("%Y-%m-%d %H:%M:%S")
            result = {
                'user': res['user'],
                'action': res['action'],
                'date': date
            }
            return JSONResponse({'result': result})
        return JSONResponse({'result': 'None'})
    except Exception as ex:
        return JSONResponse({'result': "not founded"})


async def insert(request):
    username = request.path_params['username']
    value = request.path_params['value']
    document = {'key': 'value'}
    result = await app.state.db['history'].insert_one({'user': username, 'value': value, 'key': 'value'})
    return JSONResponse({'result': result})

my_routes = [
    Route('/find/{username}', find),
    Route('/insert/{username}/{value}', insert),
]


app = Starlette(debug=True, routes=my_routes, on_startup=[connect])
