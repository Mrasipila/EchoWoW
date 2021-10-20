from abc import ABC, abstractmethod


# Recorder for screen thread object
class Recorder_m(ABC):

    @abstractmethod
    def record_m(self):
        pass

    @abstractmethod
    def join_m(self):
        pass