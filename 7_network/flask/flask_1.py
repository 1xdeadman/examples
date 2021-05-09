# flask - https://flask.palletsprojects.com/
# gunicorn - https://docs.gunicorn.org/en/latest/design.html

from flask import Flask
from flask import jsonify


# экземпляр приложения
# https://flask.palletsprojects.com/en/1.1.x/api/#flask.Flask
app = Flask(__name__)


# указывает url, по которому срабатывает данная функция
# http://127.0.0.1:5000/
# https://flask.palletsprojects.com/en/1.1.x/api/#flask.Flask.route
@app.route('/')
def home():
    # возвращаем ответ в формате json
    return jsonify({
        "res": "welcome home, the samurai"
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0')
