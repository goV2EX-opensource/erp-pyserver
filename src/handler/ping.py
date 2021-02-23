import tornado.concurrent
import tornado.gen
from tornado.web import RequestHandler
from common.Executor import Executor
import time


class PingHandler(RequestHandler):
    executor = Executor()

    def initialize(self, pingword):
        self.pingword = pingword

    @tornado.gen.coroutine
    def get(self):
        result = yield self._process(self.pingword)
        self.write(result)

    @tornado.concurrent.run_on_executor
    def _process(self, pingword):
        time.sleep(10)
        return pingword
