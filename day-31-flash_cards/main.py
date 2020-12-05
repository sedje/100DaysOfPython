from tkinter import *
from random import choice
import pandas
import os

BACKGROUND_COLOR = "#B1DDC6"
FONT_ITALIC = ("Arial", 30, "italic")
FONT = ("Arial", 35, "bold")
WAIT_TIME = 2000
flip_timer = None
word = None


# The flash-card reader takes two columns and shows heading as title and column values as content
def main():
    global flip_timer, word
    window = Tk()
    try:
        data = pandas.read_csv("data/still_to_learn.csv")
    except FileNotFoundError:
        data = pandas.read_csv("data/learn_list.csv")
    to_learn = data.to_dict(orient="records")

    def flip_card(english_word):
        canvas.itemconfig(card, image=card_back)
        canvas.itemconfig(language, text=data.columns[1], fill="white")
        canvas.itemconfig(word_label, text=english_word, fill="white")

    def next_word():
        global flip_timer, word
        window.after_cancel(flip_timer)
        try:
            word = choice(to_learn)
        except IndexError:
            canvas.itemconfig(card, image=card_front)
            canvas.itemconfig(language, text=data.columns[0], fill="black")
            canvas.itemconfig(word_label, text="learned all words!", fill="black")
            os.remove("data/still_to_learn.csv")
            window.after(WAIT_TIME, window.quit)
        else:
            canvas.itemconfig(card, image=card_front)
            canvas.itemconfig(language, text=data.columns[0], fill="black")
            canvas.itemconfig(word_label, text=word[data.columns[0]], fill="black")
            flip_timer = window.after(WAIT_TIME, flip_card, word[data.columns[1]])

    def remove_card():
        global word
        to_learn.remove(word)
        learn_data = pandas.DataFrame(to_learn)
        learn_data.to_csv("data/still_to_learn.csv", index=False)
        next_word()

    # Configure the window
    window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
    window.title("FlashCards")
    canvas = Canvas(bg=BACKGROUND_COLOR)
    canvas.config(width=800, height=526, highlightthickness=0, border=0)

    # Create all objects for the canvas
    card_front = PhotoImage(file="images/card_front.png")
    card_back = PhotoImage(file="images/card_back.png")
    card = canvas.create_image(5, 5, anchor=NW, image=card_front)
    image_ok = PhotoImage(file="images/right.png")
    button_ok = Button(image=image_ok, highlightthickness=0, border=0, command=remove_card)
    image_fail = PhotoImage(file="images/wrong.png")
    button_fail = Button(image=image_fail, highlightthickness=0, border=0, command=next_word)

    # Place all items on the grid
    canvas.grid(column=0, row=0, columnspan=3, sticky=E+W)
    language = canvas.create_text(400, 160, text=data.columns[0], font=FONT_ITALIC)
    word_label = canvas.create_text(400, 260, text="word", font=FONT)
    button_ok.grid(column=0, row=1)
    button_fail.grid(column=2, row=1)

    flip_timer = window.after(0, next_word)
    window.mainloop()


if __name__ == "__main__":
    main()
