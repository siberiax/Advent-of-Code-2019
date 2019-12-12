import sys

data = open(sys.argv[1]).read()

size = 25*6

layers = [data[i:i+size] for i in range(0, len(data) - 1, size)]

min_zeroes = min([(l.count("0"), l) for l in layers])[1]

# print(min_zeroes.count("1") * min_zeroes.count("2"))

image = ""

for i in range(size):
    start = 0
    while layers[start][i] == "2":
        start += 1
    if  layers[start][i] == "1":
        image += "0"
    else:
        image += ' '

rows = [image[i:i+25] for i in range(0, len(image) - 1, 25)]

for r in rows:
    print(r)
