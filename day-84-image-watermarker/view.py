import tkinter as tk
from PIL import ImageTk


class ImageViewer(tk.Toplevel):
    def __init__(self, master):
        tk.Toplevel.__init__(self, master)
        self.picture = None
        self.protocol('WM_DELETE_WINDOW', self.master.destroy)
        self.title("WaterMarker")
        self.geometry("1400x800")
        self.canvas = tk.Canvas(self, width=1200, height=800)
        self.canvas.place(x=120, y=0)
        self.canvas.pack()
        self.control_panel = tk.Canvas(self, height=800, width=120)
        self.control_panel.place(x=0, y=0)
        self.imageButton = tk.Button(self, text='Image', width=8)
        self.imageButton.place(x=10, y=100)
        self.addMarkButton = tk.Button(self, text='Add Mark', width=8)
        self.addMarkButton.place(x=10, y=160)
        self.saveButton = tk.Button(self, text='Save file', width=8)
        self.saveButton.place(x=10, y=190)

    def show_image(self, file=None, image=None):
        if file:
            self.picture = ImageTk.PhotoImage(image=file)
            self.canvas.create_image(0, 0, anchor='nw', image=self.picture)
        elif image:
            self.picture = image
            self.canvas.create_image(0, 0, anchor='nw', image=self.picture)
        self.canvas.update()
