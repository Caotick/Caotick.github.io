from bs4 import BeautifulSoup
from urllib.request import Request, urlopen
import re

urls = []
with open('urls.txt') as f:
    urls = f.read().splitlines()

last_chapters = []

for url in urls :
    req = Request(url, headers={'User-Agent': 'Mozilla/6.0'})
    html_page = urlopen(req).read()
    soup = BeautifulSoup(html_page, 'html.parser')
    soup_str = str(soup)
    reg = re.compile('Chapter [1-9]+')
    chap_list = [float(x.split()[-1]) for x in reg.findall(soup_str)]
    last_chapter = max(chap_list)
    last_chapters.append(int(last_chapter) if last_chapter.is_integer() else last_chapter)

with open("last_chapters.txt", "w") as f:
    for l in last_chapters :
        f.write(f"{l}\n")