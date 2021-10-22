import win32gui

# Stores the window's position value and handle value
class WindowInfo:

    def __init__(self, wndn : str):
        # window name we want the handle for
        self.wndn = wndn
        # handle to the window
        self.hwnd = None
        # positions
        self.x = None
        self.y = None
        self.w = None
        self.h = None
        # setting our classes values
        win32gui.EnumWindows(self.winEnumHandler, None)

    # saves the hwnd value
    def winEnumHandler(self, hwnd, ctx):
        if win32gui.IsWindowVisible(hwnd) and win32gui.GetWindowText(hwnd) == self.wndn:
            rect = win32gui.GetWindowRect(hwnd)
            self.set_x(rect[0])
            self.set_y(rect[1])
            self.set_h(rect[2] - self.get_x())
            self.set_w(rect[3] - self.get_y())
            self.set_hwnd(hex(hwnd))

    # getter of our class

    def get_hwnd(self):
        return self.hwnd

    def get_x(self):
        return self.x

    def get_y(self):
        return self.y

    def get_w(self):
        return self.w

    def get_h(self):
        return self.h

    # setter of our class
    def set_hwnd(self, value):
        self.hwnd = value

    def set_x(self, value):
        self.x = value

    def set_y(self, value):
        self.y = value

    def set_h(self, value):
        self.h = value

    def set_w(self, value):
        self.w = value
