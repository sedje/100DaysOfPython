import requests
from datetime import *


def main():

    parameters = {
        "lat": "52.156113",
        "lng": "5.387827",
    }
    response = requests.get(url="https://api.sunrise-sunset.org/json", params=parameters)
    try:
        response.raise_for_status()
    except requests.exceptions.HTTPError:
        print("Error")
    else:
        data = response.json()
        print(data)
        lights_on = datetime.strptime(data["results"]["sunrise"], '%I:%M:%S %p').time()
        lights_off = datetime.strptime(data["results"]["civil_twilight_end"], '%I:%M:%S %p').time()
        print(lights_off.hour)
        #print(lights_off)


if __name__ == '__main__':
    main()
