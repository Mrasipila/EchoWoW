from recorder.abstract_recorder import Recorder
from utils.checker import Checker

class Launcher:

    # The recorder stated in the constructor is supposed to be checked by the "checker" thread (master_recorder) to
    # see if it is running in order to stop the other recorders (slave_recorder).
    def __init__(self, recorder: Recorder):
        self.checker = Checker(recorder)
        self.checker.get_thread().start()

    # Launcher for recorder
    @staticmethod
    def launch(recorder: Recorder):
        thread = recorder.record()
        thread.start()

    # stop the sequential execution of the code until release
    @staticmethod
    def stop_sequential(recorder: Recorder):
        thread = recorder.record()
        thread.join()
