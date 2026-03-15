with open("python.txt", "a") as f:
    f.write(" I added a new sentence in this file.")

with open("python.txt") as f:
    print(f.read())