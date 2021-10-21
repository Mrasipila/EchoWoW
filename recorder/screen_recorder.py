from recorder.abstract_recorder import Recorder
from vidgear.gears import ScreenGear
from vidgear.gears import WriteGear
import cv2
import numpy as np
import threading

exit_key = 27  # ESC key


class Screen_Recorder(Recorder):

    def __init__(self):
        self.thread = threading.Thread(target=self.process)
        self.stopped = False
        self.data = []

    def record(self):
        return self.thread

    def get_stopped(self):
        return self.stopped

    def stop_thread(self):
        pass

    def process(self):

        buff = None
        # define dimensions of screen w.r.t to given monitor to be captured
        #options = {'top': 10, 'left': 20, 'width': 100, 'height': 100}

        # define suitable FFmpeg parameters(such as framerate) for writer
        output_params = {"-input_framerate": 20, "-c":"h264"}

        # open video stream with defined parameters
        stream = ScreenGear(monitor=1, logging=True).start()

        # Define writer with defined parameters and suitable output filename for e.g. `Output.mp4`
        writer = WriteGear(output_filename='Recording.mp4', logging=True, **output_params)

        # Specify resolution
        #resolution = (1280, 720)

        # Specify video codec
        #codec = cv2.VideoWriter_fourcc(*"mp4v")
        #filename = "Recording.mp4"

        # Specify frames rate.
        #fps = 20.0

        # Creating a VideoWriter object
        #out = cv2.VideoWriter(filename, codec, fps, resolution)

        # Create an Empty window
        cv2.namedWindow("Live", cv2.WINDOW_NORMAL)

        # Resize this window
        #cv2.resizeWindow("Live", 1280, 720)

        while True:
            # Take screenshot using PyAutoGUI
            # this screenshot is of dimension the resolution of the monitor
            #img = pyautogui.screenshot()

            frame = stream.read()

            #if frame is None:
            #   frame = buff

            #buff = frame
            # Convert the screenshot to a numpy array
            #frame = np.array(img)

            #print(frame.shape)


            #print(frame.shape)
            # Convert it from BGR(Blue, Green, Red) to
            # RGB(Red, Green, Blue)
            #frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

            # Write it to the output file
            #frame = cv2.resize(frame, resolution, interpolation=cv2.INTER_AREA)

            #out.write(frame)

            writer.write(frame)

            # Display the recording screen
            # cv2.imshow('Live', frame)

            # Stop recording when we press 'ESC'
            if  cv2.waitKey(1) == exit_key:
                self.stopped = True
                break


        # Release the Video writer
        #out.release()

        # safely close video stream
        stream.stop()

        # safely close writer
        writer.close()

        # Destroy all windows
        cv2.destroyAllWindows()

        print("screen job ended")
