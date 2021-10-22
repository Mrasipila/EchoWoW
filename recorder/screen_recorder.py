from recorder.abstract_recorder import Recorder
from vidgear.gears import ScreenGear
from vidgear.gears import WriteGear
import cv2
import numpy as np
import threading
import os
from os.path import exists
import subprocess

exit_key = 27  # ESC key


class Screen_Recorder(Recorder):

    def __init__(self):
        self.thread = threading.Thread(target=self.process)
        self.stopped = False
        self.data = []

    def record(self):
        return self.thread

    def get_stopped(self):
        return self.stopped

    def stop_thread(self):
        pass

    def process(self):
        os.chdir('F:/Dossier Personnel/AI/EchoWoW-data')
        x = 0
        filename = ""
        while True:
            filename = "output" + str(x) + ".mkv"
            if exists(filename):
                x += 1
            else:
                break
        subprocess.call(['ffmpeg', '-f', 'gdigrab', '-framerate','10','-i','desktop','F:/Dossier Personnel/AI/EchoWoW-data/'+filename])
#ffmpeg -f gdigrab -framerate 10 -i desktop [output]