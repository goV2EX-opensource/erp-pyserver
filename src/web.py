#!/usr/bin/env python3
import tornado.ioloop, tornado.gen, tornado.concurrent
from tornado.web import RequestHandler, Application
import time
from concurrent.futures import ThreadPoolExecutor
from config.config import Config


class Executor(ThreadPoolExecutor):
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not getattr(cls, '_instance', None):
            cls._instance = ThreadPoolExecutor(max_workers=Config.MAX_WORKER)
        return cls._instance


class PingHandler(RequestHandler):
    executor = Executor()

    def initialize(self, word):
        self.word = word

    @tornado.gen.coroutine
    def get(self):
        result = yield self._process(self.word)
        self.write(result)

    @tornado.concurrent.run_on_executor
    def _process(self, word):
        time.sleep(1)
        return word

word = "Hello World"
application = Application([
    (r'/ping', PingHandler, dict(word=word)),
])

if __name__ == '__main__':
    application.listen(Config.LISTEN_PORT)
    tornado.ioloop.IOLoop.current().start()
