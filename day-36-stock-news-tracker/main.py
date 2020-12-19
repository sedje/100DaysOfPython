import os
import requests
import datetime
from twilio.rest import Client
from twilio.http.http_client import TwilioHttpClient
from dotenv import load_dotenv

STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"
DOWN_SYMBOL = "⬇️"
UP_SYMBOL = "⬆️"
MAX_ARTICLES = 3
MAX_CHANGE = 10


def send_text(message):
    account_sid = os.environ['TWILIO_SID']
    auth_token = os.environ['TWILIO_AUTH']
    my_phone = os.environ['MY_PHONE']
    from_phone = os.environ['TWILIO_PHONE']
    if "PYTHONANYWHERE_DOMAIN" in os.environ:
        proxy_client = TwilioHttpClient()
        proxy_client.session.proxies = {'https': os.environ['https_proxy']}
    else:
        proxy_client = None

    client = Client(account_sid, auth_token, http_client=proxy_client)

    message = client.messages.create(
        body=message,
        from_=from_phone,
        to=my_phone
    )
    print(message.status)


def check_prices(symbol):
    stock_key = os.environ['ALPHA_KEY']
    parameters = {
        "function": "TIME_SERIES_DAILY",
        "symbol": symbol,
        "outputsize": "compact",
        "apikey": stock_key
    }
    stock_endpoint = "https://www.alphavantage.co/query"
    data = requests.get(stock_endpoint, params=parameters)
    data.raise_for_status()
    try:
        stock_prices = [values for (date, values) in data.json()["Time Series (Daily)"].items()]
        yesterday = float(stock_prices[0]['4. close'])
        day_before = float(stock_prices[1]['4. close'])
        change_percent = ((float(yesterday) - day_before) / day_before) * 100
    except KeyError:
        change_percent = 0

    return change_percent


def get_news(symbol):
    news_endpoint = "https://newsapi.org/v2/everything"
    news_key = os.environ['NEWS_KEY']
    start_date = datetime.date.today() + datetime.timedelta(days=-1)
    headers = { "X-API-KEY": news_key}
    parameters = {
        "q": symbol,
        "from": start_date,
        "sortBy": "popularity"
    }
    data = requests.get(news_endpoint, params=parameters, headers=headers)
    data.raise_for_status()
    articles = [article for article in data.json()['articles'][:MAX_ARTICLES]]
    return articles


def main():
    load_dotenv(os.path.join('./', '.env'))

    # Get closing prices and check for differences, send news items if difference bigger than 10%
    change_percent = check_prices(STOCK_NAME)
    if change_percent >= MAX_CHANGE:
        news = get_news(STOCK_NAME)
        for article in news:
            message = (f"{STOCK_NAME} {UP_SYMBOL} {change_percent:.2f}\n Headline: {article['title']}, "
                       f"brief:{article['description']} URL:{article['url']}")
            print(message)
            send_text(message)
    elif change_percent <= -MAX_CHANGE:
        news = get_news(STOCK_NAME)
        for article in news:
            message = (f"{STOCK_NAME} {DOWN_SYMBOL} {change_percent:.2f}\n Headline: {article['title']}, "
                       f"brief:{article['description']} URL:{article['url']}")
            print(message)
            send_text(message)
    else:
        print(f"No relevant news for {STOCK_NAME}, only {change_percent:.2f} changed")


if __name__ == '__main__':
    main()
