from collections import deque

def iob(i, j):
    return 0<=i<N and 0<=j<N


def bfs(si, sj, ti, tj):
    global ans

    arr = [lst[:] for lst in board]
    arr[ti][tj] = M
    q = deque()
    q.append((si, sj, 0))
    visited = [[0 for _ in range(N)] for _ in range(N)]
    visited[si][sj] = 1

    while q:
        ci, cj, time = q.popleft()
        if(ci, cj) == (N-1, N-1):
            ans = min(ans, time)
            continue

        for di, dj in DIR:
            ni, nj = ci+di, cj+dj
            if not iob(ni, nj): continue
            if visited[ni][nj] == 0 or visited[ni][nj] > time:

                if arr[ci][cj] == 1 and arr[ni][nj] > 1:  # 오작교를 건너보자
                    tmp_value = time+(arr[ni][nj]-time%arr[ni][nj])
                    visited[ni][nj] = tmp_value
                    q.append((ni, nj, tmp_value))

                elif arr[ni][nj] == 1:  # 일반 땅을 건너보자
                    visited[ni][nj] = time + 1
                    q.append((ni, nj, time+1))


N, M = map(int, input().split())
tmp = [list(map(int, input().split())) for _ in range(N)]
DIR = [(-1, 0), (0, 1), (1, 0), (0, -1)]
ans = 1e9

board = [lst[:] for lst in tmp]
for i in range(N):
    for j in range(N):
        if tmp[i][j] != 0: continue
        f_1, f_2 = False, False
        for di, dj in ((0, 1), (0, -1)):
            ni, nj = i+di, j+dj
            if not iob(ni, nj): continue
            if tmp[ni][nj] == 0:
                f_1 = True
        for ddi, ddj in ((1, 0), (-1, 0)):
            nni, nnj = i+ddi, j+ddj
            if not iob(nni, nnj): continue
            if tmp[nni][nnj] == 0:
                f_2 = True
        if f_1 and f_2:
             board[i][j] = -1  # 지나갈 수 없는 교차로

for i in range(N):
    for j in range(N):
        if board[i][j] != 0: continue
        bfs(0, 0, i, j)
print(ans)