import os
from twilio.rest import Client
from twilio.http.http_client import TwilioHttpClient


class NotificationManager:

    def __init__(self):

        self.account_sid = os.environ['TWILIO_SID']
        self.auth_token = os.environ['TWILIO_AUTH']
        self.my_phone = os.environ['MY_PHONE']
        self.from_phone = os.environ['TWILIO_PHONE']
        if "PYTHONANYWHERE_DOMAIN" in os.environ:
            self.proxy_client = TwilioHttpClient()
            self.proxy_client.session.proxies = {'https': os.environ['https_proxy']}
        else:
            self.proxy_client = None

    def send_text(self, message):
        client = Client(self.account_sid, self.auth_token, http_client=self.proxy_client)

        message = client.messages.create(
            body=message,
            from_=self.from_phone,
            to=self.my_phone
        )
        print(message.status)
