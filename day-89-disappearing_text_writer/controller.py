import tkinter as tk
from view import TypeView
from model import Timer


class TypeController:
    def __init__(self):
        self.root = tk.Tk()
        self.canvas = tk.Canvas(self.root)
        self.typeview = TypeView(self.root)
        self.timer = Timer(self.root, self.typeview)
        self.root.bind("<Key>", self.key_pressed)

    def key_pressed(self):
        if self.timer.get_time() > 0:
            self.timer.restart()
        else:
            self.timer.__init__(self.root, self.typeview)
            self.timer.run()

    def run(self):
        self.root.title("Disappearing text editor")
        self.root.deiconify()
        self.timer.run()
        self.root.mainloop()
