import tkinter as tk
from view import WordView, HighScoreView, TimerView
from model import WordList, HighScore, Timer


class Controller:
    def __init__(self):
        self.root = tk.Tk()
        self.canvas = tk.Canvas(self.root)
        self.canvas.grid(column=1, row=1)
        # Column 1
        self.wordlist = WordList()
        self.view1 = WordView(self.root)
        self.view1.set_line(self.wordlist.get_newline())
        self.timer_view = TimerView(self.root)
        self.timer = Timer(self.root, self.timer_view)
        # Column 2
        self.highscore = HighScore()
        self.highscoreview = HighScoreView(self.root)
        self.resetButton = tk.Button(self.canvas, text='Reset', command=self.reset_all)
        self.resetButton.grid(column=1, row=0)
        self.root.bind("<Key>", self.key_pressed)
        self.view1.set_word(self.wordlist.get_word())

    def key_pressed(self, event):
        if self.timer.get_time() > 0:
            if event.keysym == 'space' or event.keysym == 'Return':
                if self.wordlist.check_word(self.view1.get_word()):
                    self.highscore.increase_highscore(len(self.view1.get_word()))

                self.view1.set_word(self.wordlist.get_word())
                self.view1.set_line(self.wordlist.get_current_line())
                self.highscoreview.set_score(self.highscore.get_highscore())
        else:
            self.view1.reset()

    def reset_all(self):
        self.wordlist.__init__()
        self.highscore.__init__()
        self.timer.__init__(self.root, self.timer_view)
        self.view1.set_line(self.wordlist.get_newline())
        self.view1.set_word(self.wordlist.get_word())
        self.highscoreview.set_score(self.highscore.get_highscore())
        self.timer.reduce_time()

    def run(self):
        self.root.title("TYPOMIZER")
        self.root.deiconify()
        self.timer.reduce_time()
        self.root.mainloop()
