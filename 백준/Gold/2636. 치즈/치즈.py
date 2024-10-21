
from collections import deque

def noob(i, j):
    return 0<=i<N and 0<=j<M

def melt():
    q = deque()
    visited = [[False for _ in range(M)] for _ in range(N)]
    si, sj = 0, 0
    visited[si][sj] = True
    q.append((si, sj))
    tmp = []

    while q:
        ci, cj = q.popleft()
        for di, dj in DIR:
            ni, nj = ci+di, cj+dj
            if noob(ni, nj) and not visited[ni][nj]:
                if board[ni][nj] == 0:
                    visited[ni][nj] = True
                    q.append((ni, nj))
                elif board[ni][nj] == 1:
                    visited[ni][nj] = True
                    tmp.append((ni, nj))

    for x, y in tmp:
        board[x][y] = 0
    return


N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
tmp = sum(board, [])
cheese = tmp.count(1)
time = 0
DIR = [(-1, 0), (0, 1), (1, 0), (0, -1)]

while 1:
    melt()
    time += 1
    tmp = sum(board, [])
    if tmp.count(1) == 0:
        break
    else:
        cheese = tmp.count(1)

print(time, cheese, sep="\n")