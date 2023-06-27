import re
from bs4 import BeautifulSoup
import requests

url = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

response = requests.get(url)
movies_webpage = response.text

soup = BeautifulSoup(movies_webpage, "html.parser")

movie_titles = [movie.getText() for movie in soup.find_all("h3", class_="title")]

sorted_movie_titles = sorted(movie_titles, key=lambda x: int(re.search(r"\d+", x).group()))

print(sorted_movie_titles)

with open("movie_list.txt", "w") as file:
    file.write("\n".join(sorted_movie_titles))
