import requests
from bs4 import BeautifulSoup


def scrape_billboard(date):
    url = f"https://www.billboard.com/charts/hot-100/{date}"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    playlist = soup.find_all(class_="chart-element__information")
    songs = []
    for song in playlist:
        artist = song.find(class_="chart-element__information__artist").getText()
        song = song.find(class_="chart-element__information__song").getText()
        songs.append(f"{artist} - {song}")

    return songs


def main():
    songs = scrape_billboard("2010-08-12")
    print(songs)
    pass


if __name__ == '__main__':
    main()
