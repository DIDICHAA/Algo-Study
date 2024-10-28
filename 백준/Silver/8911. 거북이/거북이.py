def move(command):
    global si, sj, d

    if command == 'F':
        di, dj = DIR[d]
        si, sj = si+di, sj+dj
        lst.add((si, sj))

    elif command == 'B':
        di, dj = DIR[(d-2)%4]
        si, sj = si+di, sj+dj
        lst.add((si, sj))

    elif command == 'L':
        d = (d-1)%4

    else:
        d = (d+1)%4

    return


def calcul():
    max_x, max_y, min_x, min_y = -1e9, -1e9, 1e9, 1e9

    for x, y in lst:
        max_x, max_y = max(max_x, x), max(max_y, y)
        min_x, min_y = min(min_x, x), min(min_y, y)

    height = abs(max_y) + abs(min_y)
    width = abs(max_x) + abs(min_x)

    return height*width


T = int(input())
for tc in range(T):
    si, sj = 0, 0
    DIR = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    d = 0
    lst = set()
    lst.add((si, sj))
    commands = list(map(str, input().strip()))
    for command in commands:
        move(command)
    lst = list(lst)
    print(calcul())
