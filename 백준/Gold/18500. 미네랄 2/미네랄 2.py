from collections import deque

def noob(i, j):
    return 0<=i<R and 0<=j<C

def throw(i):
    global d

    if d == 0:  # if left
        for j in range(C):
            if cave[i][j] == '.': continue
            cave[i][j] = '.'
            break
        d = 1
    else:
        for j in range(C-1, -1, -1):
            if cave[i][j] == '.': continue
            cave[i][j] = '.'
            break
        d = 0
    return


def find_cluster(si, sj):
    q = deque()
    visited[si][sj] = True
    q.append((si, sj))
    tmp = [[si, sj]]

    while q:
        ci, cj = q.popleft()
        for di, dj in DIR:
            ni, nj = ci+di, cj+dj
            if noob(ni, nj) and not visited[ni][nj] and cave[ni][nj] == 'x':
                visited[ni][nj] = True
                q.append((ni, nj))
                tmp.append([ni, nj])
    return tmp


def gravity(lst):
    global cave
    lst.sort(reverse=True)  # 밑바닥에서부터 아래로 이동 가능한 지 확인
    while 1:
        change = []
        tmp = [row[:] for row in cave]
        for x, y in lst:
            if not noob(x+1, y) or tmp[x+1][y] == 'x':
                return
            elif noob(x+1, y) and tmp[x+1][y] == '.':
                tmp[x+1][y] = 'x'
                tmp[x][y] = '.'
                change.append([x+1, y])
                visited[x+1][y] = True

        cave = tmp
        lst = change


R, C = map(int, input().split())
cave = [list(map(str, input().strip())) for _ in range(R)]
N = int(input())
commands = list(map(lambda x:R-int(x), input().split()))
DIR = [(-1, 0), (0, 1), (1, 0), (0, -1)]
d = 0  # 0 is left, 1 is right

for command in commands:
    throw(command)
    visited = [[False for _ in range(C)] for _ in range(R)]
    for i in range(R-1, -1, -1):
        for j in range(C):
            if visited[i][j]: continue
            if cave[i][j] == '.': continue
            lst = find_cluster(i, j)
            gravity(lst)

for lst in cave:
    for n in lst:
        print(n, end="")
    print()