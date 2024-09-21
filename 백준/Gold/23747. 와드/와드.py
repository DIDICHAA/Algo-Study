from collections import deque


def noob(i, j):
    return 0<=i<R and 0<=j<C


def ward(ssi, ssj, group):
    # 현재 좌표 기준 같은 넘버인 애들 전부 밝혀주기
    q = deque()
    visited[ssi][ssj] = True
    q.append((ssi, ssj))
    grid[ssi][ssj] = '.'

    while q:
        ci, cj = q.popleft()
        for di, dj in DIR:
            ni, nj = ci+di, cj+dj
            if noob(ni, nj) and not visited[ni][nj] and grid[ni][nj] == group:
                visited[ni][nj] = True
                q.append((ni, nj))
                grid[ni][nj] = '.'
    return


R, C = map(int, input().split())
grid = [list(map(str, input().strip())) for _ in range(R)]
si, sj = map(int, input().split())
si -= 1
sj -= 1
commands = list(map(str, input().strip()))
DIR = [(0, 1), (0, -1), (1, 0), (-1, 0)]
DIR_2 = {'U':(-1, 0), 'D':(1, 0), 'L':(0, -1), 'R':(0, 1)}
visited = [[False] * C for _ in range(R)]
# 여기서 200,000번이 worst case
for command in commands:
    if command == 'W':
        if grid[si][sj] != '.':
            ward(si, sj, grid[si][sj])
    else:
        di, dj = DIR_2[command]
        si += di
        sj += dj

grid[si][sj] = '.'
for di, dj in DIR:
    ni, nj = si+di, sj+dj
    if noob(ni, nj):
        grid[ni][nj] = '.'

for lst in grid:
    for n in lst:
        if n != '.':
            print('#', end="")
        else:
            print('.', end="")
    print()