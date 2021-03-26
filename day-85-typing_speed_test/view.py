import tkinter as tk


# WordView, monitor for space being pressed, then send back to controller to check for word
class WordView:
    def __init__(self, master):
        self.canvas = tk.Canvas(master)
        self.canvas.grid(column=0, row=0)
        self.current_word = tk.Label(self.canvas, text="")
        self.current_word.grid(column=3, row=0, pady=20, padx=20)
        self.wordlist = tk.Text(self.canvas, height=3, width=80)
        self.textbox = tk.Text(self.canvas, height=1, width=80)
        self.wordlist.grid(column=0, row=2, columnspan=6)
        self.textbox.grid(column=0, row=3, columnspan=6)

    def set_word(self, word):
        self.textbox.delete(1.0, tk.END)
        self.current_word.config(text=word)

    def get_word(self):
        return self.textbox.get("1.0", tk.END)

    def set_line(self, line):
        self.wordlist.delete(1.0, tk.END)
        self.wordlist.insert(tk.END, " ".join(line))

    def get_line(self):
        return self.wordlist.get("1.0", tk.END)

    def reset(self):
        self.wordlist.delete(1.0, tk.END)
        self.textbox.delete(1.0, tk.END)
        self.current_word.config(text="")


class HighScoreView:
    def __init__(self, master):
        self.score = tk.Canvas(master)
        self.score.grid(column=1, row=0, pady=0, padx=0)
        self.title = tk.Label(self.score, text="ScoreBoard")
        self.title.grid(column=1, row=1, pady=20, padx=20)
        self.score_label = tk.Label(self.score, text="000000000")
        self.score_label.grid(column=1, row=2, pady=20, padx=20)

    def set_score(self, score):
        self.score_label.config(text=f"Words correct: {score[0]}\nCPM: {score[1]}")
