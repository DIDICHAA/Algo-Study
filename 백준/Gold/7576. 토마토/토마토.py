from collections import deque

def bfs():
    q = deque()
    v = [[0]*M for _ in range(N)]
    cnt = 0

    for i in range(N):
        for j in range(M):
            if tomato[i][j] == 1:
                v[i][j] = 1
                q.append((i, j))
            elif tomato[i][j] == 0:
                cnt += 1

    while q:
        si, sj = q.popleft()

        for di, dj in dir:
            ni, nj = si+di, sj+dj
            if 0<=ni<N and 0<=nj<M and v[ni][nj] == 0 and tomato[ni][nj] == 0:
                v[ni][nj] = v[si][sj] + 1
                q.append((ni, nj))
                cnt -= 1

    if cnt > 0:
        return -1
    else:
        return v[si][sj] - 1


M, N = map(int, input().split())
tomato = [list(map(int, input().split())) for _ in range(N)]
dir = [(0, 1), (0, -1), (1, 0), (-1, 0)]

print(bfs())