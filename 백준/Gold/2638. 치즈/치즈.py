from collections import deque

def iob(i, j):
    return 0<=i<N and 0<=j<M

def find_outside():
    global outside

    q = deque()
    visited = set()
    q.append((0, 0))
    visited.add((0, 0))
    outside.add((0, 0))

    while q:
        ci, cj = q.popleft()
        for di, dj in DIR:
            ni, nj = ci+di, cj+dj
            if not iob(ni, nj): continue
            if (ni, nj) in visited: continue
            if board[ni][nj] != 0: continue
            q.append((ni, nj))
            visited.add((ni, nj))
            outside.add((ni, nj))


def melt():
    global outside

    tmp = []
    q = deque()
    visited = set()

    for i in range(N):
        for j in range(M):
            if board[i][j] == 1:
                q.append((i, j))
                visited.add((i, j))

    while q:
        cnt = 0
        ci, cj = q.popleft()
        for di, dj in DIR:
            ni, nj = ci+di, cj+dj
            if not iob(ni, nj): continue
            if (ni, nj) in visited: continue
            if (ni, nj) not in outside: continue
            cnt += 1
        if cnt >= 2:
            tmp.append((ci, cj))

    if tmp:
        for x, y in tmp:
            board[x][y] = 0
        return True
    else:
        return False

N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
DIR = [(-1, 0), (0, 1), (1, 0), (0, -1)]
outside = set()
time = 0

while 1:
    find_outside()
    if not melt(): break
    time += 1

print(time)