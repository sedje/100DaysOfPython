import configparser
import requests
import time
from datetime import datetime

MY_LAT = 52.156113  # Your latitude
MY_LONG = 5.387827  # Your longitude


def is_near():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    try:
        response.raise_for_status()
    except requests.exceptions.HTTPError:
        print("Error")
    else:
        data = response.json()
        iss_latitude = float(data["iss_position"]["latitude"])
        iss_longitude = float(data["iss_position"]["longitude"])

    if MY_LAT-5 <= iss_latitude <= MY_LAT+5 and MY_LONG-5 <= iss_longitude <= MY_LONG+5:
        return True
    return False


def is_overhead():
    parameters = {
        "lat": MY_LAT,
        "lng": MY_LONG,
    }

    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise = datetime.strptime(data["results"]["sunrise"], '%I:%M:%S %p').time()
    sunset = datetime.strptime(data["results"]["sunset"], '%I:%M:%S %p').time()

    time_now = datetime.now()
    if is_near() and (time_now.hour >= sunset.hour and time_now.minute > sunset.minute
                      or
                      time_now.hour <= sunrise.hour and time_now.minute < sunrise.minute):
        return True
    else:
        return False


def mail(subject, message, recipient):
    cp = configparser.RawConfigParser()
    cp.read(cp.configFilePath('config.py'))
    my_email = cp.get('EMAIL', 'EMAIL')
    username = cp.get('EMAIL', 'EMAIL_USERNAME')
    password = cp.get('EMAIL', 'EMAIL_PASSWORD')
    subject = f"Subject:{subject}\n\n"
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=username, password=password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs=recipient,
            msg=f"{subject}{message}")


def main():
    while True:
        time.sleep(60)
        if is_overhead():
            mail("Look up!", "The ISS is over your head right now!", "mail@example.com")


if __name__ == '__main__':
    main()
