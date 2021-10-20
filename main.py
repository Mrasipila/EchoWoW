import threading
import sys
# we import our public classes
from recorder.keys_recorder import Keys_Recorder
from recorder.screen_recorder import Screen_Recorder
from recorder.mouse_recorder import Mouse_recorder
from recorder.launcher import Launcher
import gc
import cv2

#def start_thread(recorder: Recorder):
#    recorder.start()


if __name__ == "__main__":

    # as a security we unable garbage collection
    gc.enable()

    # we instantiate our classes
    screen_recorder = Screen_Recorder()
    mouse_recorder = Mouse_recorder()
    keyboard_recorder = Keys_Recorder()

    # we instantiate our recorder launcher
    launcher = Launcher(screen_recorder)

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
