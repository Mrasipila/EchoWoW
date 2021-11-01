import cv2
import numpy as np
from utils.csv_writer import CsvWriter

class ImageToVideo:

    def __init__(self, nb_images, duration, resolution, left_crop, right_crop, top_crop, bottom_crop):
        # On definie le writer
        frame_rate = float(nb_images)/duration

        print("framerate : " + str(frame_rate))
        print("nb_image : " + str(nb_images))
        print("duration : " + str(duration))
        self.out = cv2.VideoWriter('project.avi', cv2.VideoWriter_fourcc('M', 'J', 'P', 'G'), round(frame_rate), resolution)

        # setting up crops
        self.crop_right = right_crop
        self.crop_left = left_crop
        self.crop_top = top_crop
        self.crop_bottom = bottom_crop

        # writing the framerate to csvfile
        self.csv_writer = CsvWriter()
        self.csv_writer.save_frame_rate(frame_rate, duration, nb_images);


    def write_image(self, image):
        image = self.crop_image(image)
        self.out.write(cv2.cvtColor(np.array(image), cv2.COLOR_RGB2BGR))

    def crop_image(self, image):
        return cv2.cvtColor(np.array(image.crop((self.crop_left,
                                                 self.crop_top,
                                                 self.crop_right,
                                                 self.crop_bottom))), cv2.COLOR_RGB2BGR)

    def end_job(self):
        self.out.release()
