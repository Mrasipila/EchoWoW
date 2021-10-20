# check the status of the screen record stopped attribute with the view to stop the other processes
import threading
from recorder.abstract_recorder import Recorder
import time

class Checker:

    # constructor
    def __init__(self, master_recorder: Recorder, slave_recorders : list[Recorder]):
        self.thread = threading.Thread(target=self.check)
        self.master_recorder = master_recorder
        self.slave_recorders = slave_recorders

    # getter
    def get_thread(self):
        return self.thread

    # checking if master has stopped, if true we close the program.
    def process(self):
        time.sleep(2)
        if self.master_recorder.get_stopped():
            for e in self.slave_recorders:
                e.stop_thread()
                e.

    # process executed by thread
    def check(self):
        while True:
            self.process()
