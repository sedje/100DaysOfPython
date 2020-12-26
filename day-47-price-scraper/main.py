import requests
from bs4 import BeautifulSoup
import sqlite3
from datetime import datetime


def check_prices():
    conn = sqlite3.connect("pricewatch.db")
    cursor = conn.execute("SELECT product, price FROM prices;")
    for row in cursor:
        product = row[0]
        stored_price = row[1]
        current_price = get_price(product)
        if stored_price != current_price:
            print("NEW PRICE!", end=" ")
            conn.execute(f"UPDATE prices SET price = {current_price} WHERE product = '{product}'")
            conn.execute(f"INSERT INTO price_history (product, date_change, old_price, new_price) VALUES"
                         f"('{product}','{datetime.today()}',{stored_price},{current_price})")
            conn.commit()
        print(f"{' '.join(product.split('+')).title()} : {stored_price} => {current_price}")

    conn.close()


def get_price(product):
    url = f"https://www.mediamarkt.nl/nl/search.html?query={product}&searchProfile=onlineshop&channel=mmnlnl"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    price = soup.find(class_="price")

    if "-" in price.getText():
        myprice = price.getText().replace("-", "0")
    else:
        myprice = price.getText()

    return float(myprice.replace(",", "."))


def main():
    check_prices()


if __name__ == '__main__':
    main()
