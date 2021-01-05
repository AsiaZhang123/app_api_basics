from tornado.wsgi import WSGIContainer
from tornado.httpserver import HTTPServer
from tornado.ioloop import IOLoop

from app_portal import app


def main():
    http_server = HTTPServer(WSGIContainer(app))
    http_server.listen(1224)
    IOLoop.instance().start()

if __name__ == '__main__':
    main()