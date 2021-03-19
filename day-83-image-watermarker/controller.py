from tkinter import filedialog
from PIL import Image, ImageDraw
from view import ImageViewer as View
from model import Model


WATERMARK_RESIZE_FACTOR = 6

class ImageController:
    def __init__(self, root):
        self.model = Model()
        self.view1 = View(root)
        self.view1.imageButton.config(command=self.open_image)
        self.view1.addMarkButton.config(command=self.add_mark)
        self.view1.saveButton.config(command=self.save_image)

    def open_image(self):
        try:
            self.model.set_picture(filedialog.askopenfilename())
        except (FileNotFoundError, AttributeError):
            image = Image.new('RGB', (200, 30))
            d = ImageDraw.Draw(image)
            d.text((10, 10), "Image not found", fill=(255, 255, 0))
            self.model.set_picture(image)

        self.view1.show_image(file=self.model.get_picture())

    def add_mark(self):
        watermark = Image.open(filedialog.askopenfilename())
        watermark = watermark.resize((watermark.width // WATERMARK_RESIZE_FACTOR,
                                      watermark.height // WATERMARK_RESIZE_FACTOR))

        image = self.model.get_picture()
        
        # Always put watermark in lower right corner
        image.paste(watermark, (image.width-watermark.width, image.height-watermark.height), watermark.convert('RGBA'))
        self.view1.show_image(file=self.model.get_picture())

    def save_image(self):
        filename = filedialog.asksaveasfile(mode='w', defaultextension=".jpg")
        if not filename:
            return
        try:
            self.model.get_picture().save(filename)
        finally:
            exit(0)
