import os
import requests
from twilio.rest import Client
from twilio.http.http_client import TwilioHttpClient
from dotenv import load_dotenv


def send_text(message):
    account_sid = os.environ['TWILIO_SID']
    auth_token = os.environ['TWILIO_AUTH']
    my_phone = os.environ['MY_PHONE']
    from_phone = os.environ['TWILIO_PHONE']
    try:
        environment = os.environ['PYTHONANYWHERE_DOMAIN']
        proxy_client = TwilioHttpClient()
        proxy_client.session.proxies = {'https': os.environ['https_proxy']}
    except KeyError:
        proxy_client = None

    client = Client(account_sid, auth_token, http_client=proxy_client)

    message = client.messages.create(
        body=message,
        from_=from_phone,
        to=my_phone
    )
    print(message.status)


def get_weather(city):
    wd_key = os.getenv("WD_KEY")
    city_name = city
    endpoint = "http://api.openweathermap.org/data/2.5/weather"
    parameters = {"q": city_name,
                  "appid": wd_key
                  }
    weather = requests.get(endpoint, params=parameters).json()
    print(weather["weather"][0]["main"])


def main():
    load_dotenv(os.path.join('./', '.env'))
    wd_key = os.getenv("WD_KEY")
    parameters = {"appid": wd_key,
                  "lat": 52.16,
                  "lon": 5.39,
                  # "lat": 51.621441,
                  # "lon": -3.943646,
                  "exclude": "minutely,daily,current"
                  }
    endpoint = f"http://api.openweathermap.org/data/2.5/onecall"
    weather = requests.get(endpoint, params=parameters)
    weather.raise_for_status()
    weather_data = weather.json()
    rain = False
    for hour_data in weather_data['hourly'][:12]:
        if hour_data["weather"][0]["id"] < 700:
            rain = True

    if rain:
        send_text("Its gonna rain, make sure to bring an umbrella")
    else:
        send_text("No rain expected for today!")


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # get_weather("Amersfoort,NL")
    main()

