from gevent.pywsgi import WSGIServer
from webapp import create_app

app = create_app('config.ProdConfig')
server = WSGIServer(('', 80), app)
server.serve_forever()
