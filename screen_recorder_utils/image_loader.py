from PIL import Image
import os
import numpy as np
from screen_recorder_utils.image_to_video import ImageToVideo

class ImageLoader:

    def __init__(self):
        self.image_number = 0
        self.shape = None
        self.image_to_video = None


    def load_images(self, directory : str, duration : float):
        # directory must contain the path to the img_data file given by ImageSaver() class
        isFile = os.path.isfile(directory + str("/img_data0.csv"))
        if isFile is False:
            print("ERROR : no img csv file found in directory : refer to class ImageLoader")
            return
        else:
            self.set_image_number(len([img_f for img_f in os.listdir(directory)]))

            # retrieving image width and height to setup crop variable of ImageToVideo class
            array = np.loadtxt(directory + f"/img_data0.csv")
            array = array.reshape(self.get_shape())
            im = Image.fromarray(np.uint8(array))
            width, height = im.size

            # instantiate the ImageToVideo class
            self.image_to_video = ImageToVideo(nb_images=self.get_image_number(),
                                               duration=duration,
                                               resolution=(1280, 720),
                                               left_crop=8,
                                               right_crop=width-8,
                                               top_crop=39,
                                               bottom_crop=height)

            # converting the image loaded to a video
            for i in range(self.get_image_number()):
                array = np.loadtxt(directory + f"/img_data{i}.csv")
                array = array.reshape(self.get_shape())

                # change it to PIL Image for the use of the crop() method
                im = Image.fromarray(np.uint8(array))
                self.image_to_video.write_image(im)
            self.image_to_video.end_job()



    def set_image_number(self, img_nb : int):
        self.image_number = img_nb

    def set_shape(self, shape):
        self.shape = shape

    def get_image_number(self):
        return self.image_number

    def get_shape(self):
        return self.shape

