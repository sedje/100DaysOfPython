import tkinter as tk
from controller import ImageController


def main():
    root = tk.Tk()
    root.withdraw()
    app = ImageController(root)
    root.mainloop()


if __name__ == '__main__':
    main()
