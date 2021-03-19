from PIL import Image


class Model:
    def __init__(self):
        self.image = None

    def get_picture(self):
        if self.image:
            return self.image

    def set_picture(self, picture):
        self.image = Image.open(picture)

    def get_picture_size(self):
        if self.image:
            return self.image.height, self.image.width