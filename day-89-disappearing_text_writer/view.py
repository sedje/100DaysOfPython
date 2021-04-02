import tkinter as tk


class TypeView:
    def __init__(self, window):
        self.textfield = tk.Text()
        self.textfield.grid()

    def delete_all(self):
        self.textfield.delete(1.0, tk.END)
