from recorder.abstract_recorder import Recorder
from pynput import keyboard
import time


class Keys_Recorder(Recorder):

    def __init__(self):
        self.instance = keyboard.Listener(on_press=self.on_press)

    # return a thread of the executing processes
    def record(self):
        return self.instance

    # overridden methods of the library pynput
    @staticmethod
    def on_press(key):
        try:
            print('alphanumeric key {0} pressed'.format(
                key.char))
        except AttributeError:
            print('special key {0} pressed'.format(
                key))