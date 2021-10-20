from abc import ABC, abstractmethod


# Recorder for pynput thread object (mouse and keyboard)
class Recorder(ABC):

    def __init__(self):
        self.data = None
        self.data_click = None
        self.data_scroll = None

    @abstractmethod
    def record(self):
        pass

    @abstractmethod
    def get_stopped(self):
        pass