from collections import deque

def iob(i, j):
    return 0<=i<H and 0<=j<W

def bfs():
    q = deque()
    visited = [[False for _ in range(W)] for _ in range(H)]
    cnt = 0

    for x, y in candidate:
        q.append((x, y))
        visited[x][y] = True

    while q:
        ci, cj = q.popleft()
        if ci % 2 == 0:
            DIR = DIR_2
        else:
            DIR = DIR_1

        for di, dj in DIR:
            ni, nj = ci+di, cj+dj
            if not iob(ni, nj): continue
            if visited[ni][nj]: continue
            if board[ci][cj] == 0:
                if board[ni][nj] == 0:
                    visited[ni][nj] = True
                    q.append((ni, nj))
                else:
                    cnt += 1

    return cnt


W, H = map(int, input().split())
board = [[0] * (W+2)]
for _ in range(H):
    row = [0] + list(map(int, input().split())) + [0]
    board.append(row)
board.append([0] * (W+2))
W, H = W+2, H+2
DIR_1 = [(-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (0, -1)]
DIR_2 = [(-1, 0), (0, 1), (1, 0), (1, -1), (0, -1), (-1, -1)]
candidate = set()

for i in range(H):
    candidate.add((i, 0))
    candidate.add((i, W-1))
for j in range(W):
    candidate.add((0, j))
    candidate.add((H-1, j))

print(bfs())