import re
from bs4 import BeautifulSoup
import requests

response = requests.get(
    "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/")
movies_webpage = response.text

soup = BeautifulSoup(movies_webpage, "html.parser")
movie_titles = [movie.getText() for movie in soup.find_all(name="h3", class_="title")]
sorted_movie_titles = sorted(movie_titles, key=lambda x: int(re.search(r"\d+", x).group()))
print(sorted_movie_titles)

with open("movie_list.txt", "w") as file:
    for movie in sorted_movie_titles:
        file.write(f"{movie}\n")
