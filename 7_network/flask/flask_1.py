# flask - https://flask.palletsprojects.com/
# # инфа про http: https://developer.mozilla.org/ru/docs/Web/HTTP/Overview
# gunicorn - https://docs.gunicorn.org/en/latest/design.html


# Django
# Flask
# AioHTTP
# Sanic
# Tornado
# starlette

from flask import Flask


# экземпляр приложения
# https://flask.palletsprojects.com/en/1.1.x/api/#flask.Flask
app = Flask(__name__)


# указывает url, по которому срабатывает данная функция
# http://127.0.0.1:5000/
# https://flask.palletsprojects.com/en/1.1.x/api/#flask.Flask.route
@app.route('/')
def home():
    # возвращаем ответ в формате json
    return {
        "res": "welcome home, the samurai!"
    }


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
