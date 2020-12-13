from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"
FONT = ("Arial", 20, "italic")
SCORE_FONT = ("Arial", 18, "italic")


class QuizInterface:

    def __init__(self, quiz_brain: QuizBrain):
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)
        self.quiz = quiz_brain

        # SCORING PANEL
        self.scoreboard = Label()
        self.scoreboard.config(text=f"Score: {self.quiz.score}", bg=THEME_COLOR, font=SCORE_FONT, fg="white")
        self.scoreboard.grid(column=1, row=0)

        # QUESTION_CANVAS
        self.canvas = Canvas()
        self.canvas.config(width=300, height=250, highlightthickness=0, border=0, bg="white")
        self.canvas.grid(column=0, row=1, columnspan=2, sticky=E + W, pady=20)
        self.question_text = self.canvas.create_text(150, 125, width=280, text="text ajksdhsfkjshfd", font=FONT)

        # BUTTONS
        image_ok = PhotoImage(file="images/true.png")
        image_fail = PhotoImage(file="images/false.png")
        self.button_ok = Button(image=image_ok, highlightthickness=0, border=0, command=self.true_button)
        self.button_fail = Button(image=image_fail, highlightthickness=0, border=0, command=self.false_button)
        self.button_ok.grid(column=0, row=2, padx=20, pady=20)
        self.button_fail.grid(column=1, row=2)

        # RUN WINDOW
        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="white")
        self.scoreboard.config(text=f"Score: {self.quiz.score}/{len(self.quiz.question_list)}")
        if self.quiz.still_has_questions():
            self.canvas.itemconfig(self.question_text, text=self.quiz.next_question())
        else:
            self.canvas.itemconfig(self.question_text, text="End of the quiz!")
            self.button_fail.config(state="disabled")
            self.button_ok.config(state="disabled")

    def true_button(self):
        answer = self.quiz.check_answer("True")
        self.check_answer(answer)

    def false_button(self):
        answer = self.quiz.check_answer("False")
        self.check_answer(answer)

    def check_answer(self, answer):
        if answer:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.canvas.after(2000, self.get_next_question)
