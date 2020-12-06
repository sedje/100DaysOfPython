import pandas
import smtplib
import os
import datetime as dt
from random import choice


def get_quote():
    with open("quotes.txt") as quotes:
        quote_list = quotes.readlines()
    return choice(quote_list)


def mail(subject, message, recipient):
    my_email = os.getenv('EMAIL')
    username = os.getenv('EMAIL_USERNAME')
    password = os.getenv('EMAIL_PASSWORD')
    subject = f"Subject:{subject}\n\n"
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=username, password=password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs=recipient,
            msg=f"{subject}{message}")


def send_quotes():
    now = dt.datetime.now()
    if now.isoweekday() == 7:
        mail("quotes", get_quote(), "mail@example.com")


def check_birthdays():
    now = dt.datetime.now()
    birthdays = pandas.read_csv("birthdays.csv")
    for key, value in birthdays.iterrows():
        if value['day'] == now.day and value['month'] == now.month:
            letter = choice(os.listdir("letter_templates"))
            with open("letter_templates/"+letter) as letter:
                letter_content = letter.read()
                letter_content = letter_content.replace("[NAME]", value['name'])
            mail("Birthday", letter_content, value['email'])


if __name__ == '__main__':
    send_quotes()
    check_birthdays()
