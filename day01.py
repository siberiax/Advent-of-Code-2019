data = open('input.txt', 'r+').read().split()

x = 0
for line in data:
    y = int(line)
    while 1:
        y //= 3
        y -= 2
        if y > 0:
            x += y
        else:
            break

print(x)
