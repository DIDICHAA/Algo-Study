from collections import deque

def iob(i, j):
    return 0<=i<R and 0<=j<C


def bfs(si, sj):
    q = deque()
    visited = [[0 for _ in range(C)] for _ in range(R)]
    for x, y in fire:
        q.append((x, y))
        visited[x][y] = 1
    q.append((si, sj))
    visited[si][sj] = 1

    while q:
        ci, cj = q.popleft()
        for di, dj in DIR:
            ni, nj = ci+di, cj+dj

            if board[ci][cj] == '.' and not iob(ni, nj):
                return True, visited[ci][cj]

            if not iob(ni, nj): continue
            if visited[ni][nj] != 0: continue
            if board[ni][nj] != '.': continue

            if board[ci][cj] == 'F':
                board[ni][nj] = 'F'
            visited[ni][nj] = visited[ci][cj] + 1
            q.append((ni, nj))

    return False, -1


R, C = map(int, input().split())
board = [list(map(str, input())) for _ in range(R)]
DIR = [(-1, 0), (0, 1), (1, 0), (0, -1)]
fire = []

for i in range(R):
    for j in range(C):
        if board[i][j] == 'J':
            board[i][j] = '.'
            si, sj = i, j
        elif board[i][j] == 'F':
            fire.append([i, j])

flag, time = bfs(si, sj)
if flag:
    print(time)
else:
    print('IMPOSSIBLE')