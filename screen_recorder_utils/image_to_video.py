import cv2
import numpy as np

class ImageToVideo:

    def __init__(self,fr, resolution, left_crop, right_crop, top_crop, bottom_crop):
        # On definie le writer
        self.out = cv2.VideoWriter('project.avi', cv2.VideoWriter_fourcc('M', 'J', 'P', 'G'), round(fr), resolution)

        # setting up crops
        self.crop_right = right_crop
        self.crop_left = left_crop
        self.crop_top = top_crop
        self.crop_bottom = bottom_crop

    def write_image(self, image):
        image = self.crop_image(image)
        self.out.write(image)

    def crop_image(self,image):
        return cv2.cvtColor(np.array(image.crop((self.crop_left,
                                                  self.crop_top,
                                                  self.crop_right,
                                                  self.crop_bottom))), cv2.COLOR_RGB2BGR)

    def end_job(self):
        self.out.release()