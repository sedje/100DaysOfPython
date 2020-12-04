from tkinter import *
from tkinter import messagebox
from random import choice
from pyperclip import copy
import json
import string

# INSECURE VERSION OF A PASSWORD MANAGER OF COURSE. DON'T SAVE PASSWORDS     #
# WITHOUT ENCRYPTION.... EVER!                                               #
PASSWORD_FILE = "myPasswords.json"


def main():

    def search_password():
        try:
            with open(PASSWORD_FILE, 'r') as password_file:
                data = json.load(password_file)
                if website_entry.get() in data:
                    username_entry.insert(0, data[website_entry.get()]['username'])
                    pw_entry.insert(0, data[website_entry.get()]['password'])
        except FileNotFoundError as e:
            print(f"File not found: {e.filename}")

    # ---------------------------- PASSWORD GENERATOR ------------------------------- #
    def generate_password():
        """generate a random password"""
        password_list = [choice(string.ascii_letters+string.digits+string.punctuation) for _ in range(16)]
        password = ''.join(password_list)
        # Use pyperclip to copy the password to clipboard
        copy(password)
        pw_entry.insert(0, password)

    # ---------------------------- SAVE PASSWORD ------------------------------- #
    def save_password():
        """Ask for verification and save password entry to file"""
        website = website_entry.get()
        username = username_entry.get()
        password = pw_entry.get()

        if len(website) == 0 or len(password) == 0 or len(username) == 0:
            messagebox.showerror("Oops", "Not all values are filled out correctly")
        else:
            # Check if the user really wants to enter this combination
            message = f"Website: {website}\nUsername: {username}\nPassword: {password}"
            confirm = messagebox.askquestion("Are you sure?", message)

            if confirm == "yes":
                entry = {
                    website: {
                        'username': username,
                        'password': password
                    },
                }
                try:
                    with open(PASSWORD_FILE, 'r') as myPasswords:
                        data = json.load(myPasswords)
                        data.update(entry)
                except (json.decoder.JSONDecodeError, FileNotFoundError):
                    with open(PASSWORD_FILE, 'w') as myPasswords:
                        json.dump(entry, myPasswords, indent=4)
                else:
                    with open(PASSWORD_FILE, 'w') as myPasswords:
                        json.dump(data, myPasswords, indent=4)
                finally:
                    # Clear all entries for re-entry
                    website_entry.delete(0, END)
                    # username_entry.delete(0, END)
                    pw_entry.delete(0, END)

    # ---------------------------- UI SETUP ------------------------------- #
    window = Tk()
    window.title("Password Manager")
    window.config(padx=50, pady=50)
    canvas = Canvas(width=200, height=200)
    background = PhotoImage(file='logo.png')
    canvas.create_image(200, 112, image=background, anchor=CENTER)

    # website label + entry
    website_label = Label()
    website_label.config(text="Website:")
    website_entry = Entry()
    website_search = Button(text="search websites", command=search_password)
    website_entry.grid(column=1, row=1)
    website_search.grid(column=2, row=1)
    website_label.grid(column=0, row=1)
    # email/username label + entry
    username_label = Label()
    username_label.config(text="Email/Username:")
    username_entry = Entry()
    username_entry.grid(column=1, row=2, columnspan=2, sticky=E+W)
    username_label.grid(column=0, row=2)
    # password label + entry + generate_button
    pw_label = Label()
    pw_label.config(text="Password:")
    pw_entry = Entry()
    generate = Button(text="Generate Password", command=generate_password)
    pw_entry.grid(column=1, row=3)
    pw_label.grid(column=0, row=3)
    generate.grid(column=2, row=3)
    # add button
    add_pw = Button(text="Add", command=save_password)
    add_pw.grid(column=1, row=4, columnspan=4, sticky=E+W)
    canvas.grid(column=0, row=0, columnspan=4, sticky=E+W)
    window.mainloop()


if __name__ == '__main__':
    main()
