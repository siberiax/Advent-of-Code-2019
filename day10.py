import sys

data = [line.strip() for line in open(sys.argv[1])]

highest  =  0
best = ""

for x in range(len(data)):
    for y in range(len(data[0])):
        if data[x][y] == '.':
            continue

        asteroids = set()

        for i in range(len(data)):
            for j in range(len(data[0])):
                if data[i][j] == '.':
                    continue
                elif i == x and j == y:
                    continue
                elif j == y:
                    if i < x:
                        asteroids.add('a')
                    else:
                        asteroids.add('b')
                elif i == x:
                    if j < y:
                        asteroids.add('l')
                    else:
                        asteroids.add('r')
                else:

                    delta_x = i-x
                    delta_y = j-y
                    slope = str(delta_x/delta_y)

                    if i < x and j < y:
                        slope += 'bl'
                    elif i > x and j > y:
                        slope += 'bg'
                    elif i < x and j > y:
                        slope += 'jg'
                    else:
                        slope += 'lg'

                    asteroids.add(slope)

        if len(asteroids) > highest:
            highest = len(asteroids)
            best = ((y,x))

print(highest)
print(best)
