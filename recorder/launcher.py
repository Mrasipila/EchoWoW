from recorder.abstract_recorder import Recorder


class Launcher:

    def __init__(self):
        self.launcher = None

    def launch(self,recorder: Recorder):
        recorder.record().start()
