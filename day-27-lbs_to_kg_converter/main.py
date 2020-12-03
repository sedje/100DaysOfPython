from tkinter import *


def main():
    def lbs_to_kg(*args):
        kgs = round(float(lbs.get())/2.205)
        kilos_result.configure(text=f'{kgs}')

    window = Tk()
    window.title("LBS to KG converter")
    window.minsize(width=300, height=100)
    window.maxsize(width=300, height=100)
    window.configure(padx=10, pady=10)
    weight_label = Label(text="Weight in lbs")
    button = Button(text="Calculate", command=lbs_to_kg)
    window.bind("<Return>", lbs_to_kg)
    window.bind("<KP_Enter>", lbs_to_kg)
    kilos_label = Label(text="Weight in kilos")
    kilos_result = Label(text="~")
    lbs = Entry()

    weight_label.grid(column=0, row=0)
    lbs.grid(column=2, row=0)
    kilos_label.grid(column=0, row=1)
    kilos_result.grid(column=2, row=1)
    button.grid(column=1, row=2, columnspan=2)
    lbs.focus()
    window.mainloop()


if __name__ == '__main__':
    main()
