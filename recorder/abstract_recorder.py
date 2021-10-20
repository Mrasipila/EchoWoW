from abc import ABC, abstractmethod


class Recorder(ABC):

    @abstractmethod
    def record(self):
        pass
