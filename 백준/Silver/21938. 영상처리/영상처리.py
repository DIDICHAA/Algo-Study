from collections import deque

def oob(i, j):
    return 0<=i<N and 0<=j<M*3 and monitor[i][j] == 255

def find_thing(si, sj):
    q = deque()
    visited[si][sj] = 1
    q.append((si, sj))

    while q:
        ci, cj = q.popleft()
        for di, dj in dir:
            ni, nj = ci+di, cj+dj
            if oob(ni, nj) and visited[ni][nj] == 0:
                visited[ni][nj] = 1
                q.append((ni, nj))


N, M = map(int, input().split())
monitor = [list(map(int, input().split())) for _ in range(N)]
T = int(input())
# M *= 3

visited = [[0]*(M*3) for _ in range(N)]
dir = [(0, 1), (0, -1), (1, 0), (-1, 0)]
cnt = 0

lst_1 = []
lst_2 = []

for i in range(N):
    for j in range(0, M*3, 3):
        num = monitor[i][j:j+3]
        avg = sum(num) / 3

        if avg < T:
            lst_1.append((i, j))
            lst_1.append((i, j+1))
            lst_1.append((i, j+2))
        else:
            lst_2.append((i, j))
            lst_2.append((i, j+1))
            lst_2.append((i, j+2))

for i, j in lst_1:
    monitor[i][j] = 0
for i, j in lst_2:
    monitor[i][j] = 255

for i in range(N):
    for j in range(M*3):
        if monitor[i][j] == 255 and visited[i][j] == 0:
            find_thing(i, j)
            cnt += 1

print(cnt)