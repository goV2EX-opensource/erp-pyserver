from concurrent.futures import ThreadPoolExecutor

from config.config import Config


class Executor(ThreadPoolExecutor):
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not getattr(cls, '_instance', None):
            cls._instance = ThreadPoolExecutor(max_workers=Config.MAX_WORKER)
        return cls._instance