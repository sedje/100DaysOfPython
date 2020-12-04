from tkinter import *
import math

PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None


def main():
    # ---------------------------- TIMER RESET ------------------------------- #
    def reset_timer():
        global reps, timer
        reps = 0
        window.after_cancel(timer)
        canvas.itemconfig(timer_text, text=f"00:00")
        pomodoro.config(text="️")

    # ---------------------------- TIMER MECHANISM ------------------------------- #
    def start_timer():
        global reps
        reps += 1
        if reps % 8 == 0:
            label.config(text="Long Break", fg=RED)
            add_pomodoro(math.floor(reps / 2))
            count_down(count=LONG_BREAK_MIN*60)
        elif reps % 2 == 0:
            add_pomodoro(math.floor(reps / 2))
            label.config(text="Short Break", fg=PINK)
            count_down(count=SHORT_BREAK_MIN*60)
        else:
            label.config(text="Work", fg=GREEN)
            count_down(count=WORK_MIN*60)

    def add_pomodoro(number_of_poms):
        poms = "✔️" * number_of_poms
        pomodoro.config(text=poms, fg=GREEN)
        pomodoro.update()

    # ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
    def count_down(count):
        if count > 0:
            global timer
            timer = window.after(1000, count_down, count - 1)
            minutes = int(count / 60)
            seconds = count % 60
            if seconds == 0 or seconds < 10:
                seconds = "0"+str(seconds)
            canvas.itemconfig(timer_text, text=f"{minutes}:{seconds}")
        else:
            start_timer()

    # ---------------------------- UI SETUP ------------------------------- #
    window = Tk()
    window.title("Pomodoro")
    window.config(padx=50, pady=50, bg=YELLOW)
    canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
    background = PhotoImage(file='tomato.png')
    canvas.create_image(100, 112, image=background)
    timer_text = canvas.create_text(103, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
    label = Label()
    label.config(text="Timer", font=(FONT_NAME, 35, "bold"), bg=YELLOW, fg=GREEN)
    label.grid(column=0, row=0, columnspan=3, sticky=W+E)
    pomodoro = Label()
    pomodoro.config(font=(FONT_NAME, 35, "bold"), bg=YELLOW)
    pomodoro.grid(column=1, row=2)
    start_button = Button(text="start", command=start_timer)
    reset_button = Button(text="reset", command=reset_timer)
    canvas.grid(column=1, row=1)
    start_button.grid(column=0, row=2)
    reset_button.grid(column=2, row=2)

    window.mainloop()


if __name__ == '__main__':
    main()
