# check the status of the screen record stopped attribute with the view to stop the other processes
import threading
from recorder.abstract_recorder import Recorder
import time
import os
import psutil



class Checker:

    # constructor
    def __init__(self, recorder: Recorder):
        self.thread = threading.Thread(target=self.check)
        self.recorder = recorder

    # getter
    def get_thread(self):
        return self.thread

    # checking if master has stopped, if true we close the program.
    def process(self):
        time.sleep(2)
        if self.recorder.get_stopped():
            # terminate the program process
            current_system_pid = os.getpid()
            this_system = psutil.Process(current_system_pid)
            this_system.terminate()

    # process executed by thread
    def check(self):
        while True:
            self.process()
