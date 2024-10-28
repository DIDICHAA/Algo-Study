from collections import deque

def noob(i, j):
    return 0<=i<N and 0<=j<M


def calcul(lst):
    global ans

    tmp = [row[:] for row in board]
    for x, y in lst:
        tmp[x][y] = 1

    q = deque()
    visited = [[0 for _ in range(M)] for _ in range(N)]
    for x, y in virus:
        q.append((x, y))
        visited[x][y] = 1

    while q:
        ci, cj = q.popleft()
        for di, dj in DIR:
            ni, nj = ci+di, cj+dj
            if noob(ni, nj) and not visited[ni][nj] and tmp[ni][nj] == 0:
                visited[ni][nj] = 1
                q.append((ni, nj))

    cnt = 0
    for i in range(N):
        for j in range(M):
            if visited[i][j] == 0 and tmp[i][j] == 0:
                cnt += 1
    ans = max(ans, cnt)


def make_comb(cnt, idx, lst):
    if cnt == 3:
        calcul(lst)
        return

    for i in range(idx, len(candi)):
        lst.append(candi[i])
        make_comb(cnt+1, i+1, lst)
        lst.pop()


N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
DIR = [(-1, 0), (0, 1), (1, 0), (0, -1)]
ans = 0
candi = []
virus = []
for i in range(N):
    for j in range(M):
        if board[i][j] == 0:
            candi.append([i, j])
        elif board[i][j] == 2:
            virus.append([i, j])

make_comb(0, 0, [])
print(ans)