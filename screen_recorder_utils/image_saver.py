import numpy as np


class ImageSaver():

    def __init__(self):
        self.counter = 0
        self.shape = None

    def store_data(self, image):
        image.save(f"csvfiles/img_data/img_data{self.get_counter()}.jpg")
        self.increment()

    def increment(self):
        self.counter += 1

    def get_counter(self):
        return self.counter

    def set_shape(self, shape):
        self.shape = shape
