import tkinter as tk
from view import WordView, HighScoreView
from model import WordList, HighScore


class Controller:
    def __init__(self):
        self.root = tk.Tk()
        self.canvas = tk.Canvas(self.root)
        self.canvas.grid(column=1, row=1)
        self.wordlist = WordList()
        self.highscore = HighScore()
        self.highscoreview = HighScoreView(self.root)
        self.view1 = WordView(self.root)
        self.view1.set_line(self.wordlist.get_newline())
        self.resetButton = tk.Button(self.canvas, text='Reset', command=self.reset_all)
        self.resetButton.grid(column=0, row=0)
        self.root.bind("<Key>", self.key_pressed)
        self.view1.set_word(self.wordlist.get_word())

    def key_pressed(self, event):
        if event.keysym == 'space' or event.keysym == 'Return':
            if self.wordlist.check_word(self.view1.get_word()):
                self.highscore.increase_highscore(len(self.view1.get_word()))

            self.view1.set_word(self.wordlist.get_word())
            self.view1.set_line(self.wordlist.get_current_line())
            self.highscoreview.set_score(self.highscore.get_highscore())
        else:
            pass

    def reset_all(self):
        self.view1.set_line(self.wordlist.get_newline())
        self.view1.set_word(self.wordlist.get_word())
        self.highscore.reset()
        self.highscoreview.set_score(self.highscore.get_highscore())

    def run(self):
        self.root.title("TYPOMIZER")
        self.root.deiconify()
        self.root.mainloop()
