lines = []
with open("url_mapping.txt", "r") as f:
    lines = f.read().splitlines()

names = [lines.split(',')[0] for line in lines]
urls = [lines.split(',')[1] for line in lines]

with open("names.txt", "w") as f:
    for name in names :
        f.write(f"{name}\n")

with open("urls.txt", "w") as f: 
    for url in urls :
        f.write(f"{url}\n")