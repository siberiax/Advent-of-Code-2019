import sys
from collections import defaultdict

data = [line.strip() for line in open(sys.argv[1])]

infinity = 999999999
neg_infinity = -999999999

x = 28
y = 29
destroyed = 0

all_asteroids = []

asteroids = defaultdict(list)
for i in range(0, x):
    for j in range(y, len(data[0])):
        if data[i][j] == '.':
            continue
        elif j == y:
            asteroids[infinity].append((j,i))
        else:

            delta_x = x-i
            delta_y = j-y
            slope = delta_x/delta_y

            asteroids[slope].append((j,i))

keys = reversed(sorted(asteroids.keys()))
for key in keys:
    all_asteroids.append(asteroids[key])

asteroids.clear()
for i in range(x, len(data)):
    for j in range(y + 1, len(data[0])):
        if data[i][j] == '.':
            continue
        else:
            delta_x = x-i
            delta_y = j-y
            slope = delta_x/delta_y

            asteroids[slope].append((j,i))

keys = reversed(sorted(asteroids.keys()))
for key in keys:
    all_asteroids.append(list(reversed(asteroids[key])))

asteroids.clear()
for i in range(x + 1, len(data)):
    for j in range(0, y + 1):
        if data[i][j] == '.':
            continue
        elif j == y:
            asteroids[neg_infinity].append((j,i))
        else:
            delta_x = x-i
            delta_y = j-y
            slope = delta_x/delta_y

            asteroids[slope].append((j,i))

keys = reversed(sorted(asteroids.keys()))
for key in keys:
    all_asteroids.append(list(reversed(asteroids[key])))

asteroids.clear()
for i in range(0, x+1):
    for j in range(0, y):
        if data[i][j] == '.':
            continue
        elif j == y:
            asteroids[neg_infinity].append((j,i))
        else:
            delta_x = x-i
            delta_y = j-y
            slope = delta_x/delta_y

            asteroids[slope].append((j,i))

keys = reversed(sorted(asteroids.keys()))
for key in keys:
    all_asteroids.append(asteroids[key])

i = 1
while all_asteroids:
    new = []
    for a in all_asteroids:
        if i == 200:
            c = a[-1]
            print(c[0] * 100 + c[1])
        if len(a) > 1:
            new.append(a[:-1])
        i += 1
    all_asteroids = new
