from threading import Lock

from src.utils.singleton import Singleton


class Locker(metaclass=Singleton):
    def __init__(self):
        self.lock = Lock()

    def set_acquire(self):
        self.lock.acquire()

    def set_release(self):
        self.lock.release()

    def is_locked(self):
        return self.lock.locked()

    def printID(self):
        return id(self.lock)
