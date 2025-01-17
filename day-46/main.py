from bs4 import BeautifulSoup
import requests

date = input("Which year do you want to travel to? Type the date in this format YYYY-MM-DD: ")

header = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:131.0) Gecko/20100101 Firefox/131.0"}
response = requests.get(f"https://www.billboard.com/charts/hot-100/{date}/", headers=header)
billboard_web_site = response.text
print(billboard_web_site)

soup = BeautifulSoup(billboard_web_site, "html.parser")
songs_names_spans = soup.select("li ul li h3")
song_names = [song.getText().strip() for song in songs_names_spans]
print(song_names)
