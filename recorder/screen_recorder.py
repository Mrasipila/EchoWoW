
from recorder.abstract_recorder import Recorder
import pyautogui
import cv2
import numpy as np
import threading


class Screen_Recorder(Recorder):

    def __init__(self, recorder : Recorder):
        self.thread = threading.Thread(target=self.process)

    def record(self):
        return self.thread

    @staticmethod
    def process():
        # Specify resolution
        resolution = (1280, 720)

        # Specify video codec
        codec = cv2.VideoWriter_fourcc(*"mp4v")
        filename = "../Recording.mp4"

        # Specify frames rate.
        fps = 20.0

        # Creating a VideoWriter object
        out = cv2.VideoWriter(filename, codec, fps, resolution)

        # Create an Empty window
        cv2.namedWindow("Live", cv2.WINDOW_NORMAL)

        # Resize this window
        cv2.resizeWindow("Live", 1280, 720)

        full_video = []
        while True:
            # Take screenshot using PyAutoGUI
            # this screenshot is of dimension the resolution of the monitor
            img = pyautogui.screenshot()

            # Convert the screenshot to a numpy array
            frame = np.array(img)

            # we scale down the screenshot to the desired resolution (variable resolution)
            dim = resolution
            frame = cv2.resize(frame, dim, interpolation=cv2.INTER_AREA)

            # Convert it from BGR(Blue, Green, Red) to
            # RGB(Red, Green, Blue)
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

            # Write it to the output file
            full_video.append(frame)

            # Optional: Display the recording screen
            cv2.imshow('Live', frame)

            # Stop recording when we press 'q'
            if cv2.waitKey(1) == ord('q'):
                break

        # downloding the video
        for i in range(len(full_video)):
            out.write(full_video[i])

        # Release the Video writer
        out.release()

        # Destroy all windows
        cv2.destroyAllWindows()

        print("screen job ended")

