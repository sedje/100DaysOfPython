import requests
import os
from dotenv import load_dotenv
import datetime
NUTRI_HEADERS = {}
SHEET_HEADERS = {}
EXERCISE_API = "https://trackapi.nutritionix.com/v2/natural/exercise"
SHEET_URL = ""


def set_globals():
    global NUTRI_HEADERS, SHEET_HEADERS, SHEET_URL
    try:
        load_dotenv('.env')
        app_id = os.environ['APP_ID']
        app_key = os.environ['APP_KEY']
        sheet_token = os.environ['SHEET_TOKEN']
        NUTRI_HEADERS = {"x-app-id": app_id, "x-app-key": app_key}
        SHEET_HEADERS = {"Authorization": f"Bearer {sheet_token}"}
        SHEET_URL = f"https://api.sheety.co/{os.environ['SHEET_USERNAME']}/myWorkouts/workouts"
    except (FileNotFoundError, KeyError):
        print("Either the .env file does not exist "
              "or does not contain APP_ID, APP_KEY, SHEET_TOKEN and/or SHEET_USERNAME")


def main():
    set_globals()
    get_exercise_data()
    get_sheet_data()


def get_exercise_data():
    exercise = input("What did you do today?: ")
    # exercise = "run 3 km and swim 2 km"
    parameters = {"query": exercise}
    request = requests.post(url=EXERCISE_API, json=parameters, headers=NUTRI_HEADERS)
    for result in request.json()['exercises']:
        parameters = {
            "workout": {
                "date": datetime.datetime.now().strftime("%d/%m/%Y"),
                "time": datetime.datetime.now().strftime("%H:%M:%S"),
                "exercise": str(result['name']).title(),
                "duration": result['duration_min'],
                "calories": result['nf_calories']
            }
        }
        requests.post(url=SHEET_URL, json=parameters, headers=SHEET_HEADERS)


def get_sheet_data():
    request = requests.get(url=SHEET_URL, headers=SHEET_HEADERS)
    print(request.json())


if __name__ == '__main__':
    main()
