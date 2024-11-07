from collections import deque

def iob(i, j):
    return 0<=i<N and 0<=j<N


def bfs(si, sj):
    q = deque()
    visited = [[0 for _ in range(N)] for _ in range(N)]
    for k in range(len(board[si][sj])):
        x, y = board[si][sj][k]
        check[x][y] = True
        flag = True
    if flag:
        switches[si][sj] = True
        visited[si][sj] = 1
        q.append((si, sj, 1))
    else:
        q.append((si, sj, 0))

    while q:
        ci, cj, cnt = q.popleft()
        for di, dj in DIR:
            ni, nj = ci+di, cj+dj
            if not iob(ni, nj): continue
            if not check[ni][nj]: continue
            if visited[ni][nj] >= cnt: continue

            if not switches[ni][nj]:
                for k in range(len(board[ni][nj])):
                    nx, ny = board[ni][nj][k]
                    if not check[nx][ny]:
                        check[nx][ny] = True
                visited[ni][nj] = cnt + 1
                q.append((ni, nj, cnt + 1))
                switches[ni][nj] = True

            else:
                visited[ni][nj] = cnt
                q.append((ni, nj, cnt))


N, M = map(int, input().split())
board = [[[] for _ in range(N)] for _ in range(N)]
check = [[False for _ in range(N)] for _ in range(N)]
check[0][0] = True
DIR = [(-1, 0), (0, 1), (1, 0), (0, -1)]
switches = [[False for _ in range(N)] for _ in range(N)]

for _ in range(M):
    x, y, a, b = map(lambda x:int(x)-1, input().split())
    board[x][y].append([a, b])

bfs(0, 0)
print(sum(check, []).count(True))