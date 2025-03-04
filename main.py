from bs4 import BeautifulSoup
from urllib.request import Request, urlopen
import re

url_mapping = []
with open('url_mapping.txt') as f:
    url_mapping = f.read().splitlines()

last_chapters = []

names = [x.split(",")[0] for x in url_mapping]

html = '''<!DOCTYPE html><html lang="en"><head><style>body { min-height: 100vh; } td { text-align: center; }</style></head><body><h1>Test</h1><table style="width:25%;height:150%;border:1px solid black;margin-left:auto;margin-right:auto;"><thead><th>Manga/Manhua name</th><th>Last Chapter</th></thead><tbody>'''

for i, name in enumerate(names) :
    with open(f"{name}.html", "r") as f :
        soup = BeautifulSoup(f, 'html.parser')
        soup_str = str(soup)
        reg = re.compile('Chapter [1-9]+')
        chap_list = [float(x.split()[-1]) for x in reg.findall(soup_str)]
        last_chapter = max(chap_list) if len(chap_list) > 0 else 0.0
        last_chapter = int(last_chapter) if last_chapter.is_integer() else last_chapter
        if(i%2==0) :
            html += f'''<tr style = "background-color:#badeff;"><td>{name}</td><td>{last_chapter}</td></tr>'''
        else :
            html += f'''<tr><td>{name}</td><td>{last_chapter}</td></tr>'''
        

html += '''</tbody></table></body></html>'''

with open('index.html', "w") as f :
    f.write(html)
