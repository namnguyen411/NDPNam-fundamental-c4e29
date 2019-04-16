from urllib.request import urlopen
from bs4 import BeautifulSoup
import pyexcel
from collections import OrderedDict
from youtube_dl import YoutubeDL

#1. Open connection
url = "https://www.apple.com/itunes/charts/songs"
conn = urlopen(url)
raw_data = conn.read()

html_content = raw_data.decode('utf8')

soup = BeautifulSoup(html_content, "html.parser")
section = soup.find("section", "section chart-grid")
div = section.find("div")
ul = div.find("ul")
li_list = ul.find_all("li")

list_song = []
for li in li_list:
        dict_song = {}
        h3 = li.h3
        a = h3.a 
        h4 = li.h4
        a1 = h4.a
        song_name = a.string.strip()
        artist_name = a1.string.strip()
        link = a["href"]
        dic_song = OrderedDict({
                "title" : song_name,
                "artist" : artist_name,
                "link" : link
        })
        list_song.append(dic_song)

# pyexcel.save_as(records=list_song, dest_file_name="top_song.xls")

options = {
        'default_search' : 'ytsearch',
        'max_downloads' : 1,
}

for i in range(len(list_song)):
    ytsearch = list_song[i]['title'] + list_song[i]['artist']
    dl = YoutubeDL(options)
    dl.download([ytsearch])