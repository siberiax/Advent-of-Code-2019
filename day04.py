import sys

def increasing(s):
    for i in range(len(s) - 1):
        if s[i] > s[i+1]:
            return 0
    return 1

def double(s):
    for i in range(len(s) - 1):
        if i == 0:
            if s[i] == s[i+1] != s[i+2]:
                return 1
        if i == 4:
            if s[i] == s[i+1] != s[i-1]:
                return 1
        else:
            if s[i-1] != s[i] == s[i+1] != s[i+2]:
                return 1
    return 0

start = int(sys.argv[1])
end = int(sys.argv[2])

total = 0
for i in range(start, end):

    s = str(i)
    good = 0

    if increasing(s):
        if double(s):
            good = 1

    if good:
        total += 1

print(total)
