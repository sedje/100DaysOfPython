from dotenv import load_dotenv
from notification_manager import NotificationManager
from data_manager import DataManager
from flight_search import FlightSearch
MY_LOCATION = "AMS"
MY_CITY = "Amsterdam"


def main():
    load_dotenv('.env')
    notification_manager = NotificationManager()
    data_manager = DataManager()
    # TODO: Uncomment after this month because of rate limit on sheety
    # data = data_manager.get_data()
    data = {"prices": [
                {"id": 1, "city": "Paris", "iataCode": "", "lowestPrice": 100},
                {"id": 2, "city": "Berlin", "iataCode": "", "lowestPrice": 100}
            ]}
    flight_search = FlightSearch()
    for destination in data['prices']:
        code = ""
        try:
            if destination['iataCode'] == '':
                code = flight_search.get_iata(city_name=destination['city'])
            else:
                code = destination['iataCode']
        except KeyError:
            code = flight_search.get_iata(city_name=destination['city'])
        finally:
            cheapest_flight = flight_search.get_price(origin=MY_LOCATION, destination=code)
            price = cheapest_flight['price']
            body = {
                "price": {
                    "id": destination['id'],
                    "city": destination['city'],
                    "iataCode": code,
                    "lowestPrice": price
                },
            }
            if price < destination['lowestPrice']:
                message = f"Low Price Alert: Only €{price} to fly from {MY_CITY} " \
                          f"to {destination['city']}-{cheapest_flight['flyTo']}! between " \
                          f"{cheapest_flight['utc_departure'].split('T')[0]} and " \
                          f"{cheapest_flight['utc_arrival'].split('T')[0]} "
                # TODO: Uncomment after this month because of rate limit on sheety
                print(message)
                # notification_manager.send_text(message=message)
            #data_manager.update_row(destination['id'], body)


if __name__ == "__main__":
    main()
