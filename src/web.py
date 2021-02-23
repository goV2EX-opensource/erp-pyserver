#!/usr/bin/env python3
import tornado.ioloop, tornado.concurrent
from tornado.web import Application
from config.config import Config
from handler.ping import PingHandler
from handler.avatar import AvatarHandler



pingword = "Alive"
application = Application([
    (r'/ping', PingHandler, dict(pingword=pingword)),
    (r'/avatar/(.*)', AvatarHandler, dict(StorageDriverConfig=Config.StorageDriverConfig)),
])

if __name__ == '__main__':
    application.listen(Config.LISTEN_PORT)
    tornado.ioloop.IOLoop.current().start()
