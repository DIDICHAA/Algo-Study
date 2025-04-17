from collections import deque

def noob(i, j):
    return 0<=i<N and 0<=j<M


def find_ice(si, sj):
    q = deque()
    visited[si][sj] = True
    q.append((si, sj))

    while q:
        ci, cj = q.popleft()
        for di, dj in DIR:
            ni, nj = ci+di, cj+dj
            if noob(ni, nj) and board[ni][nj] != 0 and not visited[ni][nj]:
                visited[ni][nj] = True
                q.append((ni, nj))


def melt():
    global board

    tmp = [lst[:] for lst in board]
    for i in range(N):
        for j in range(M):
            if board[i][j] == 0: continue
            cnt = 0
            for di, dj in DIR:
                ni, nj = i+di, j+dj
                if noob(ni, nj) and board[ni][nj] == 0:
                    cnt += 1
            if cnt > 0:
                tmp[i][j] -= cnt
                if tmp[i][j] <= 0:
                    tmp[i][j] = 0

    board = tmp
    return


N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
DIR = [(-1, 0), (0, 1), (1, 0), (0, -1)]
time = 0
flag = False

while 1:
    cnt = 0
    visited = [[False for _ in range(M)] for _ in range(N)]
    for i in range(N):
        for j in range(M):
            if not visited[i][j] and board[i][j] != 0:
                find_ice(i, j)
                cnt += 1
    if cnt > 1:
        flag = True
        break
    melt()
    time += 1
    if sum(sum(board, [])) == 0:
        break

if flag:
    print(time)
else:
    print(0)