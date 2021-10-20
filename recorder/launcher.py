from recorder import Recorder


class Launcher:

    @staticmethod
    def launch(recorder: Recorder):
        Recorder.record().start()
