from recorder.abstract_recorder import Recorder
from vidgear.gears import ScreenGear
from vidgear.gears import WriteGear
import cv2
import threading
from utils.window_info import WindowInfo
from exceptions.unresolved_window import UnresolvedWindow


exit_key = 27  # ESC key


class Screen_Recorder(Recorder):

    def __init__(self):
        super().__init__()
        self.thread = threading.Thread(target=self.process)
        self.stopped = False
        self.data = []
        self.window = None

        # look for window named "World Of Warcraft"
        try:
            self.window = WindowInfo("World of Warcraft")
        except UnresolvedWindow:
            raise UnresolvedWindow

    def record(self):
        return self.thread

    def get_stopped(self):
        return self.stopped

    def stop_thread(self):
        pass

    def process(self):

        print(self.window.x)
        print(self.window.y)
        # define suitable FFmpeg input parameters
        options = {"top": self.window.y, "left": self.window.x, "width": self.window.h, "height": self.window.w}

        # define suitable FFmpeg output parameters
        output_params = {"-r": 30}# "-c:v": "libx264", "-preset": "slow", "-crf": 0}

        # open video stream with defined parameters
        stream = ScreenGear(monitor=1, logging=True, **options).start()

        # Define writer with defined parameters and suitable output filename for e.g. `Output.mp4`
        writer = WriteGear(output_filename='Recording.mp4', logging=True) #, **output_params)

        # Specify resolution
        # resolution = (1280, 720)

        # Specify video codec
        # codec = cv2.VideoWriter_fourcc(*"mp4v")
        # filename = "Recording.mp4"

        # Specify frames rate.
        # fps = 20.0

        # Creating a VideoWriter object
        # out = cv2.VideoWriter(filename, codec, fps, resolution)

        # Create an Empty window
        cv2.namedWindow("Live", cv2.WINDOW_NORMAL)

        # Resize this window
        # cv2.resizeWindow("Live", 1280, 720)

        while True:
            # Take screenshot using PyAutoGUI
            # this screenshot is of dimension the resolution of the monitor
            # img = pyautogui.screenshot()

            frame = stream.read()

            # if frame is None:
            #   frame = buff

            # buff = frame
            # Convert the screenshot to a numpy array
            # frame = np.array(img)

            # print(frame.shape)

            # print(frame.shape)
            # Convert it from BGR(Blue, Green, Red) to
            # RGB(Red, Green, Blue)
            # frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

            # Write it to the output file
            # frame = cv2.resize(frame, resolution, interpolation=cv2.INTER_AREA)

            # out.write(frame)

            writer.write(frame)

            # Display the recording screen
            # cv2.imshow('Live', frame)

            # Stop recording when we press 'ESC'
            if cv2.waitKey(1) == exit_key:
                self.stopped = True
                break

        # Release the Video writer
        # out.release()

        # safely close video stream
        stream.stop()

        # safely close writer
        writer.close()

        # Destroy all windows
        cv2.destroyAllWindows()

        print("screen job ended")
