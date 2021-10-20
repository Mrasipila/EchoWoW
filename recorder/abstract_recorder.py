from abc import ABC, abstractmethod


# Recorder for pynput thread object (mouse and keyboard)
class Recorder(ABC):

    @abstractmethod
    def record(self):
        pass

    @abstractmethod
    def get_stopped(self):
        pass

    @abstractmethod
    def stop_thread(self):
        pass