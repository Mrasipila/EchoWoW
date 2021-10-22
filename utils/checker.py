import threading
from recorder.abstract_recorder import Recorder
import time
import os
import psutil
from utils.csv_writer import CsvWriter

# check the status of the screen record stopped attribute with the view to stop the other processes
class Checker:

    # constructor
    def __init__(self, master_recorder: Recorder, slaves_recorder: list[Recorder]):
        # instantiating the Checker thread
        self.thread = threading.Thread(target=self.check)
        # saving the data for slave recorder the master recorder (screen) data saving task being already handled by
        # it's thread
        # TODO : Implement savings of windows Info, Never move the window of the game once the program is
        #  running, because the window info position is not saved in time. It is only saved at the programs
        # startup we passing the slaves to save the keys and the master to save the window position of the window
        # we want to record
        self.csv_writer = CsvWriter(master_recorder, slaves_recorder)
        self.recorder = master_recorder

    # getter of the actual thread, used to start the Checker from the launcher
    def get_thread(self):
        return self.thread

    # checking if master has stopped, if true we close the program.
    def process(self):
        time.sleep(2)
        if self.recorder.get_stopped():
            # saves the data
            self.csv_writer.save_keyboard_data()
            self.csv_writer.save_mouse_data()
            self.csv_writer.save_screen_wnd()
            # terminate the program process
            current_system_pid = os.getpid()
            this_system = psutil.Process(current_system_pid)
            this_system.terminate()

    # process executed by thread
    def check(self):
        while True:
            self.process()
