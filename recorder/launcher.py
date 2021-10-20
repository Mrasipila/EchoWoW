from recorder.abstract_recorder import Recorder


class Launcher:

    def __init__(self, recorder : Recorder):
        self.launcher = Recorder.record()

    def launch(self,recorder: Recorder):
        Recorder.record(self).start()
