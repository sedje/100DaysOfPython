import requests


def _find_movie(title):
    url = "https://api.themoviedb.org/3/search/movie"
    params = {
                "api_key": "488c0e41ee63e4732492b3a7604a2624",
                "language": "en-US",
                "query": title,
                "include_adult": "false"
             }
    movie = requests.get(url, params=params).json()
    print(len(movie['results']))
    return movie['results'][0]


movie = _find_movie("Gone in 60 seconds")

title = movie['original_title']
img_url = f"https://image.tmdb.org/t/p/w300/{movie['poster_path']}"
year = movie['release_date'].split('-')[0]
description = movie['overview']

