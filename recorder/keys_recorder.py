from recorder.abstract_recorder import Recorder
from pynput import keyboard
from utils.csv_writer import CsvWriter
import datetime
import csv


class Keys_Recorder(Recorder):

    def __init__(self):
        super().__init__()
        self.instance = keyboard.Listener(on_press=self.on_press)
        self.data = []

    # return a thread of the executing processes
    def record(self):
        return self.instance

    def get_stopped(self):
        pass

    # overridden methods of the library pynput
    def on_press(self,key):
        try:
            self.data.append([key.char, datetime.datetime.now().time()])
        except AttributeError:
            self.data.append([key, datetime.datetime.now().time()])