from recorder.abstract_recorder import Recorder
import cv2
import threading
from utils.window_info import WindowInfo
from exceptions.unresolved_window import UnresolvedWindow
from mss import mss
from PIL import Image
import numpy as np
import datetime
from screen_recorder_utils.image_saver import ImageSaver
from screen_recorder_utils.image_loader import ImageLoader

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
            print("temp")
            raise UnresolvedWindow

        # ImageSaver
        self.image_saver = ImageSaver()

        # ImageLoader
        self.image_loader = ImageLoader()

    def record(self):
        return self.thread

    def get_stopped(self):
        return self.stopped

    def stop_thread(self):
        pass

    def process(self):

        # define suitable input parameters
        options = {"top": self.window.y, "left": self.window.x, "width": self.window.h, "height": self.window.w}

        cv2.namedWindow("Live", cv2.WINDOW_NORMAL)

        # beginnning of the recording
        bt = datetime.datetime.now()

        with mss() as sct:

            # retrieving data from first screenshot to set shape for image loader
            screenShot = sct.grab(options)
            img = Image.frombytes(
                'RGB',
                (screenShot.width, screenShot.height),
                screenShot.rgb,
            )
            self.image_loader.set_shape(cv2.cvtColor(np.array(img.copy()), cv2.COLOR_RGB2BGR).shape)

            while True:
                screenShot = sct.grab(options)
                img = Image.frombytes(
                    'RGB',
                    (screenShot.width, screenShot.height),
                    screenShot.rgb,
                )

                # writing the image
                self.image_saver.store_data(cv2.cvtColor(np.array(img.copy()), cv2.COLOR_RGB2BGR))

                # Live Video
                # cv2.imshow('Live', np.array(img))

                # Stop recording when we press 'ESC'
                if cv2.waitKey(1) == exit_key:
                    et = datetime.datetime.now()
                    print("exiting")
                    break

        delta_t = et - bt

        self.image_loader.load_images(directory="csvfiles/img_data", duration=float(delta_t.total_seconds()))

        # Destroy all windows
        cv2.destroyAllWindows()

        self.stopped = True

        print("Done !")
