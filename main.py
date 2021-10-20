import threading
import sys
# we import our public classes
from recorder.keys_recorder import Keys_Recorder
from recorder.screen_recorder import Screen_Recorder
from recorder.mouse_recorder import Mouse_recorder
from recorder.launcher import Launcher
from utils.csv_writer import CsvWriter
import gc
import datetime
import csv

#def start_thread(recorder: Recorder):
#    recorder.start()


if __name__ == "__main__":

    # as a security we unable garbage collection
    gc.enable()

    # time when the code launched

    f = open('csvfiles/started_at.csv', 'w+')
    writer = csv.writer(f, delimiter=" ")
    writer.writerow(str(datetime.datetime.now().time()))
    f.close()


    # we instantiate our classes
    screen_recorder = Screen_Recorder()
    mouse_recorder = Mouse_recorder()
    keyboard_recorder = Keys_Recorder()

    # we instantiate our recorder launcher
    # second argument should always start with keyboard_recorder followed with mouse_recorder
    launcher = Launcher(screen_recorder, [keyboard_recorder, mouse_recorder])

    # launching out recorders
    launcher.launch(mouse_recorder)
    launcher.launch(screen_recorder)
    launcher.launch(keyboard_recorder)

    # stopping the sequential execution of the code while the threads are running (join() method of thread)
    launcher.stop_sequential(mouse_recorder)
    launcher.stop_sequential(screen_recorder)
    launcher.stop_sequential(keyboard_recorder)



    #mouse_recorder.record().start()
    #screen_recorder.record().start()

    #mouse_recorder.record().join()
    #screen_recorder.record().join()
