import time
from pynput import mouse
from recorder.abstract_recorder import Recorder
import datetime

class Mouse_recorder(Recorder):

    def __init__(self):
        self.instance = mouse.Listener(on_move=self.on_move,
                                       on_click=self.on_click,
                                       on_scroll=self.on_scroll)
        self.data_click = []
        self.data_scroll = []

    # return a thread of the executing processes
    def record(self):
        return self.instance

    def get_stopped(self):
        pass

    # overridden methods of the library pynput
    @staticmethod
    def on_move(x, y):
        pass

    def on_click(self,x, y, button, pressed):
        print(str(x) +" "+ str(y))
        self.data_click.append([str(x), str(y), datetime.datetime.now().time()])

    def on_scroll(self,x, y, dx, dy):
        self.data_scroll.append([str(dy), datetime.datetime.now().time()])