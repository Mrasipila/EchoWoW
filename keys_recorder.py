from recorder import *
import time


class Keys_Recorder(Recorder):

    def record():
        i = 0
        while i < 3:
            print("keys")
            time.sleep(0.3)
            i += 1
