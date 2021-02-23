import os


class StorageDriver(object):
    def __init__(self, config):
        self.path = config
        pass

    def open(self, username, mode):
        print("Open File: " + os.path.join(self.path, username) + " with mode" + mode)
        return open(os.path.join(self.path, username), mode)
