
import time
from pynput import mouse
from recorder.abstract_recorder import Recorder


class Mouse_recorder(mouse.Listener, Recorder):

    def __init__(self):
        self.instance = super(Mouse_recorder, self).__init__(
            on_move=self.on_move, on_click=self.on_click, on_scroll=self.on_scroll)

    # return a thread of the executing processes
    def record(self):
        return self.instance

    # overridden methods of the library pynput
    @staticmethod
    def on_move(x, y):
        print('Pointer moved to {0}'.format(
            (x, y)))

    @staticmethod
    def on_click(x, y, button, pressed):
        print('{0} at {1}'.format(
            'Pressed' if pressed else 'Released',
            (x, y)))
        if not pressed:
            # Stop listener
            return False

    @staticmethod
    def on_scroll(x, y, dx, dy):
        print('Scrolled {0} at {1}'.format(
            'down' if dy < 0 else 'up',
            (x, y)))