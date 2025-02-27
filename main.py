with open('urls.txt') as f:
    lines = f.read().splitlines()

with open("test.txt", "w") as f :
    for line in lines :
        f.write(f"{line}\n")
