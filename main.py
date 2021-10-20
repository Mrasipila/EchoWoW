import threading

# we import our public classes
# from recorder.keys_recorder import Keys_Recorder
from recorder.screen_recorder import Screen_Recorder
from recorder.mouse_recorder import Mouse_recorder
from recorder.launcher import Launcher
import cv2

#def start_thread(recorder: Recorder):
#    recorder.start()


if __name__ == "__main__":
    # we instantiate our classes
    screen_recorder = Screen_Recorder()
    mouse_recorder = Mouse_recorder()
    #keyboard_recorder = Keys_Recorder()


    #mouse_recorder.record().start()
    #screen_recorder.record().start()

    launcher = Launcher()

    #launcher.launch_m(screen_recorder)
    launcher.launch(mouse_recorder)

