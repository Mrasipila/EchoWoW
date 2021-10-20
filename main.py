import threading

# we import our public classes
# from recorder.keys_recorder import Keys_Recorder
from recorder.screen_recorder import Screen_Recorder
from recorder.mouse_recorder import Mouse_recorder
from recorder.launcher import Launcher

#def start_thread(recorder: Recorder):
#    recorder.start()


if __name__ == "__main__":
    # we instantiate our classes
    screen_recorder = Screen_Recorder()
    mouse_recorder = Mouse_recorder()
    #keyboard_recorder = Keys_Recorder()



    launcher = Launcher()

    launcher.launch(screen_recorder)
    launcher.launch(mouse_recorder)

    # we store our three threads executing their object (aka the record methods) corresponding to the child of the
    # abstract class).
    #thread_screen = threading.Thread(target=screen_recorder.record)
    #thread_mouse = mouse_recorder.record()
    #thread_keyboard = keyboard_recorder.record()

    # we launch our threads
    #thread_screen.start()
    #thread_mouse.start()
    #thread_keyboard.start()
