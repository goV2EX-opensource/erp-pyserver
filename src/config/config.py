class Config(object):
    LISTEN_PORT = 8888
    MAX_WORKER = 10
    StorageDriverConfig = 'file://./'

    def __init__(self, config_str=None):
        pass