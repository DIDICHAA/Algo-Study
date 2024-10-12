from collections import deque

def noob(i, j):
    return 0<=i<N and 0<=j<M

def bfs(si, sj):
    global max_cnt

    q = deque()
    visited[si][sj] = True
    q.append((si, sj))
    cnt = 1

    while q:
        ci, cj = q.popleft()
        for di, dj in DIR:
            ni, nj = ci+di, cj+dj
            if noob(ni, nj) and board[ni][nj] == 1 and not visited[ni][nj]:
                visited[ni][nj] = True
                q.append((ni, nj))
                cnt += 1

    max_cnt = max(max_cnt, cnt)
    return



N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
DIR = [(-1, 0), (0, 1), (1, 0), (0, -1)]

max_cnt, pic = 0, 0
visited = [[False for _ in range(M)] for _ in range(N)]
for i in range(N):
    for j in range(M):
        if visited[i][j]: continue
        if board[i][j] == 0: continue
        bfs(i, j)
        pic += 1

if pic == 0:
    print(0, 0, sep='\n')
else:
    print(pic, max_cnt, sep="\n")