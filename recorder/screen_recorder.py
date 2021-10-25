from recorder.abstract_recorder import Recorder
import cv2
import threading
from utils.window_info import WindowInfo
from exceptions.unresolved_window import UnresolvedWindow
from mss import mss
from PIL import Image
import numpy as np
import datetime
import time

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

        bt = datetime.datetime.now()

        with mss() as sct:
            while True:
                screenShot = sct.grab(options)
                img = Image.frombytes(
                    'RGB',
                    (screenShot.width, screenShot.height),
                    screenShot.rgb,
                )

                # writing the image
                #i += 1
                #cv2.imwrite('video/img' + "%03d" % i + '.jpg', cv2.cvtColor(np.array(img.copy()), cv2.COLOR_RGB2BGR))

                images.append(img.copy())

                # Live Video
                #cv2.imshow('Live', np.array(img))


                # Stop recording when we press 'ESC'
                if cv2.waitKey(1) == exit_key:
                    et = datetime.datetime.now()
                    break

        delta_t = et-bt
        fr = float(len(images))/delta_t.total_seconds()

        out = cv2.VideoWriter('project.avi', cv2.VideoWriter_fourcc('M','J','P','G'), round(fr), (1280, 720))

        # récupère la dimension de l'image
        print(images[1].size)
        print("fr :"+ str(fr))
        print("delta_t :" + str(delta_t.total_seconds()))
        print("nb_im : " + str(len(images)))
        width, height = images[1].size
        # Setting the points for cropped image
        left = 8
        top = 39
        right = width - 8
        bottom = height
        print(images[i].crop((left, top, right, bottom)).size)

        cpt = 0
        cpt1 = 0
        for i in range(len(images)):
            if images[i] is None:
                cpt+=1
                print("None cpt : " + cpt)
            cpt1+=1
            #print(cv2.cvtColor(np.array(images[i].crop((left, top, right, bottom))),  cv2.COLOR_RGB2BGR))
            print("cpt1 :" + str(cpt1))
            # Cropped image of above dimension writen to output
            img = cv2.cvtColor(np.array(images[i].crop((left, top, right, bottom))),  cv2.COLOR_RGB2BGR)
            out.write(img)
            #cv2.imwrite('video/img' + "%03d" % i + '.jpg', img)
            print("cpt1 :" + str(cpt1))

            #print(cpt1)
            #cv2.imshow('Live', img)


        print("empty images : " + str(cpt))
        out.release()

        # Destroy all windows
        cv2.destroyAllWindows()

        self.stopped = True

        print("screen job ended")

