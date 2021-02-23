import tornado.concurrent
import tornado.gen
from tornado.web import RequestHandler
from common.Executor import Executor
import time
from PIL import Image


class AvatarHandler(RequestHandler):
    executor = Executor()

    def initialize(self, StorageDriverConfig):
        config_header = StorageDriverConfig.find('://')
        storage_driver = StorageDriverConfig[:config_header]
        self.StorageDriver = __import__("common.StorageDriver." + storage_driver, fromlist=storage_driver).\
            StorageDriver(StorageDriverConfig[config_header+3:])

    @tornado.gen.coroutine
    def get(self, uuid):
        self.set_header("Content-type", "image/jpeg")
        pics = yield self._readpic(uuid)
        self.write(pics)

    @tornado.concurrent.run_on_executor
    def _readpic(self, uuid):
        pic = self.StorageDriver.open('resources/' + uuid + '.jpg', 'rb')
        pics = pic.read()
        return pics
