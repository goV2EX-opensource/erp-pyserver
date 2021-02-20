#!/usr/bin/env python3
from abc import ABC

import tornado.ioloop, tornado.gen, tornado.concurrent
from tornado.web import RequestHandler, Application
import time
from concurrent.futures import ThreadPoolExecutor
from config.config import Config


class Executor(ThreadPoolExecutor):
    """ 创建多线程的线程池，线程池的大小为10
    创建多线程时使用了单例模式，如果Executor的_instance实例已经被创建，
    则不再创建，单例模式的好处在此不做讲解
    """
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
        time.sleep(10)
        return word


if __name__ == '__main__':
    word = "Hello World"
    app = Application([
        (r'/ping', PingHandler, dict(database=word)),
    ])
    app.listen(Config.LISTEN_PORT)
    tornado.ioloop.IOLoop.current().start()
