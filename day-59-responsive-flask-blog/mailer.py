from dotenv import load_dotenv
import smtplib
import os


class Mailer:

    def __init__(self):
        load_dotenv(".env")
        self.my_email = os.getenv('EMAIL')
        self.username = os.getenv('EMAIL_USERNAME')
        self.password = os.getenv('EMAIL_PASSWORD')

    def send_mail(self, message=""):
        subject = f"Subject:Website feedback\n\n"

        try:
            with smtplib.SMTP("smtp.gmail.com") as connection:
                connection.starttls()
                connection.login(user=self.username, password=self.password)
                connection.sendmail(
                    from_addr=self.my_email,
                    to_addrs=self.my_email,
                    msg=f"{subject}{message}")
        except smtplib.SMTPAuthenticationError:
            pass
