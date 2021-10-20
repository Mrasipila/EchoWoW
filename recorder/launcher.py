from recorder.abstract_recorder import Recorder

class Launcher:


    def __init__(self):
        self.launcher = None

    # Launcher for recorder
    def launch(self, recorder: Recorder):
        thread = recorder.record()
        thread.start()

    # stop the sequential execution of the code until release
    def stop_sequential(self, recorder: Recorder):
        thread = recorder.record()
        thread.join()
