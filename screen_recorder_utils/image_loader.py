from PIL import Image
import os
import numpy as np

class ImageLoader:

    def __init__(self, recording_time):
        self.image_number = 0
        self.shape = None
        pass

    def load_images(self, directory : str):
        # directory must contain the path to the img_data file given by ImageSaver() class
        isFile = os.path.isfile(directory + str("/img0.csv"))
        if isFile is False:
            print("ERROR : no img csv file found in directory : refer to class ImageLoader")
            return
        else:
            self.set_image_number(len([img_f for img_f in os.listdir(directory)]))
            for i in range(self.get_image_number()):
                array = np.loadtxt(directory + f"/img_data{i}.csv")
                array = array.reshape(self.get_shape())
                im = Image.fromarray(np.uint8(array))

    def set_image_number(self, img_nb : int):
        self.image_number = img_nb

    def set_shape(self, shape):
        self.shape = shape

    def get_image_number(self):
        return self.image_number

    def get_shape(self):
        return self.shape


