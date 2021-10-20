from recorder.abstract_recorder import Recorder
from recorder.abstract_recorder_m import Recorder_m

class Launcher:

    def __init__(self):
        self.launcher = None

    # Launcher for pynput thread object
    @staticmethod
    def launch(recorder: Recorder):
        recorder.record().start()


    # Launcher for non pynput thread object
    @staticmethod
    def launch_m(recorder: Recorder_m):
        recorder.record_m().start()
        recorder.join_m()