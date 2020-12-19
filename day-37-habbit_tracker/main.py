import requests
import datetime
import os
from dotenv import load_dotenv

PIXEL_ENDPOINT = "https://pixe.la/v1/users"
PIXEL_COLORS = {
    "green": "shibafu",
    "red": "momiji",
    "blue": "sora",
    "yellow": "ichou",
    "purple": "ajisai",
    "black": "kuro"
}
USERNAME = "sedje"
HEADER = ""


def set_globals():
    global USERNAME, HEADER
    load_dotenv("./.env")
    if "PIXEL_API_TOKEN" in os.environ:
        HEADER = {"X-USER-TOKEN": os.getenv("PIXEL_API_TOKEN")}
    else:
        passwd = input("Please provide a new password")
        HEADER = {"X-USER-TOKEN": passwd}
        with open(".env", "w") as environment_file:
            environment_file.write(f"export PIXEL_API_TOKEN={passwd}")
    # Check if user exists in env. variables, if not, add to file
    if "PIXEL_API_USER" not in os.environ:
        with open(".env", "a") as environment_file:
            environment_file.write(f"\nexport PIXEL_API_USER={USERNAME}")
    else:
        USERNAME = os.getenv("PIXEL_API_USER")


def main():
    set_globals()

    # Check if user exists on pixe.la, if not, register the user!
    check_user = requests.get(url=f"https://pixe.la/@{USERNAME}")
    if "not found" in check_user.text:
        register()

    # Check if graph exists, if not, create graph, if so, just add values
    if not check_graph("banana"):
        create_graph("banana", "banana", "yellow")
        add_pixel("banana", "5")
    else:
        update_pixel("banana", "3")


def check_graph(graph_name):
    graph_endpoint = f"{PIXEL_ENDPOINT}/{USERNAME}/graphs"

    request = requests.get(url=graph_endpoint, headers=HEADER)
    if graph_name in request.text:
        return True
    return False


def create_graph(graph_name, unit, color):
    graph_endpoint = f"{PIXEL_ENDPOINT}/{USERNAME}/graphs"
    parameters = {
        "id": graph_name,
        "name": graph_name,
        "unit": unit,
        "type": "int",
        "color": PIXEL_COLORS.get(color),
        "isSecret": True
    }
    requests.post(url=graph_endpoint, headers=HEADER, json=parameters)


def add_pixel(graph_name, quantity):
    graph_endpoint = f"{PIXEL_ENDPOINT}/{USERNAME}/graphs/{graph_name}"
    parameters = {
        "date": datetime.date.today().strftime("%Y%m%d"),
        "quantity": quantity
    }
    requests.post(url=graph_endpoint, headers=HEADER, json=parameters)


def update_pixel(graph_name, quantity):
    date = datetime.date.today().strftime("%Y%m%d")
    graph_endpoint = f"{PIXEL_ENDPOINT}/{USERNAME}/graphs/{graph_name}/{date}"
    parameters = {
        "quantity": quantity
    }
    requests.put(url=graph_endpoint, headers=HEADER, json=parameters)


def register():
    parameters = {
        "token": os.getenv("PIXEL_API_TOKEN"),
        "username": USERNAME,
        "agreeTermsOfService": "yes",
        "notMinor": "yes"
    }
    registration = requests.post(url=PIXEL_ENDPOINT, json=parameters)
    print(registration.text)


def delete_user():
    set_globals()
    graph_endpoint = f"{PIXEL_ENDPOINT}/{USERNAME}"
    requests.delete(url=graph_endpoint, headers=HEADER)


if __name__ == '__main__':
    # main()
    delete_user()
