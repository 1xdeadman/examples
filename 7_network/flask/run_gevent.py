from gevent.pywsgi import WSGIServer
from flask_1 import app

# запускает сервис на 5000 порту
http_server = WSGIServer(('', 5000), app)
http_server.serve_forever()
