# flask - https://flask.palletsprojects.com/
# gunicorn - https://docs.gunicorn.org/en/latest/design.html

from flask import Flask, url_for
from flask import jsonify, request, Request, Response
from markupsafe import escape

app = Flask(__name__)


def helper(value):
    res: Response = jsonify({
        "res": value + value
    })
    return res


# указывает параметры строки url
# http://127.0.0.1:5000/base/10
# https://flask.palletsprojects.com/en/1.1.x/quickstart/#variable-rules
@app.route('/base/<value>')
def base(value):
    return helper(value)


# указывает конкретный тип параметра строки url
@app.route('/test/<int:value>')
def test_var_int(value):
    return helper(value)


@app.route('/test/<string:value>')
def test_var_str(value):
    return helper(value)


# methods указывает тип запроса, который обрабатывается данной функцией
@app.route('/', methods=['GET', 'POST'])
def test():
    print(request.method)
    return jsonify({
        "res": "welcome home, the samurai!"
    })


if __name__ == '__main__':
    # запустить веб приложение в тестовом режиме.
    # https://flask.palletsprojects.com/en/1.1.x/api/#flask.Flask.run
    app.run(host='0.0.0.0', debug=True)
