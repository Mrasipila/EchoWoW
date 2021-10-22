from recorder.abstract_recorder import Recorder
import cv2
import threading
from utils.window_info import WindowInfo
from exceptions.unresolved_window import UnresolvedWindow
from mss import mss
from PIL import Image
import numpy as np

exit_key = 27  # ESC key


class Screen_Recorder(Recorder):

    def __init__(self):
        super().__init__()
        self.thread = threading.Thread(target=self.process)
        self.stopped = False
        self.data = []
        self.window = None

        # look for window named "World Of Warcraft"
        self.window = WindowInfo("World of Warcraft")
        if self.window is None:
            raise UnresolvedWindow

    def record(self):
        return self.thread

    def get_stopped(self):
        return self.stopped

    def stop_thread(self):
        pass

    def process(self):

        images = []
        i = 0

        # define suitable input parameters
        options = {"top": self.window.y, "left": self.window.x, "width": self.window.h, "height": self.window.w}

        cv2.namedWindow("Live", cv2.WINDOW_NORMAL)

        with mss() as sct:
            while True:
                screenShot = sct.grab(options)
                img = Image.frombytes(
                    'RGB',
                    (screenShot.width, screenShot.height),
                    screenShot.rgb,
                )

                cv2.imwrite('video/' + str(i) + '.jpg', cv2.cvtColor(np.array(img.copy()), cv2.COLOR_RGB2BGR))
                i += 1

                # Stop recording when we press 'ESC'
                if cv2.waitKey(1) == exit_key:
                    self.stopped = True
                    break

        out = cv2.VideoWriter('project.mp4', cv2.VideoWriter_fourcc(*'mp4v'), 1, (1280, 720))

        for i in range(len(images)):
            out.write(cv2.cvtColor(np.array(images[i]), cv2.COLOR_RGB2BGR))
        out.release()

        # Destroy all windows
        cv2.destroyAllWindows()

        print("screen job ended")
