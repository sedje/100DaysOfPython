from bs4 import BeautifulSoup
import requests


def use_bs():
    # Simple exercise to learn basics of BeautifulSoup
    with open("website.html", "r") as website:
        content = website.read()

    soup = BeautifulSoup(content, "html.parser")
    # Soup get all a h-refs and print only link.
    links = soup.find_all("a")
    for link in links:
        print(link.get("href"))

    # Soup use class_ selector
    header = soup.find(class_="heading")
    print(header.getText())

    # Soup get CSS Selector
    print(soup.select_one(selector=".heading"))

    # Soup get by nested style selectors
    print(soup.select_one(selector="p a"))


def scraping():
    # a scraper for getting y combinator news in order from lowest to highest score.
    url = "https://news.ycombinator.com/news"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")

    # Get all news IDs and item scores for further processing
    rows = soup.find_all("tr", class_="athing")
    news_ids = {}
    for row in rows:
        news_id = row.get('id')
        score_id = f"score_{news_id}"
        try:
            news_ids[news_id] = int(soup.find(id=score_id).getText().split()[0])
        except AttributeError:
            news_ids[news_id] = 0

    # Resort the news IDs based on the score
    sorted_news_ids = dict(sorted((score, news_id) for (news_id, score) in news_ids.items()))

    # Print all items in list
    for item in sorted_news_ids.items():
        news_article = soup.find(id=item[1])
        link = news_article.find("a", class_="storylink")
        print(f"score: {item[0]} : {link.getText()} - {link.get('href')}")


def main():
    # Get best movies all time from empire online
    url = "https://www.empireonline.com/movies/features/best-movies-2/"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")

    # Find all h3 tags with the class title, as they contain the movie titles and append them to a list
    titles = soup.find_all("h3", class_="title")
    to_watch = []
    for title in titles:
        if ")" in title.getText():
            to_watch.append(' '.join(title.getText().split()[1:]))
        else:
            to_watch.append(title.getText())

    # Reverse the list, as its from 100 -> 1 originally
    to_watch.reverse()

    # Write the list to a file.
    with open("To_Watch.txt", "w") as watchlist:
        for movie in to_watch:
            watchlist.write(f"{to_watch.index(movie)+1}) {movie}\n")


if __name__ == '__main__':
    # scraping()
    # use_bs()
    main()
