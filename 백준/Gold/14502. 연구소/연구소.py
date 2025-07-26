from collections import deque

def iob(i, j):
    return 0<=i<N and 0<=j<M

def find_safe_zone(c1, c2, c3):
    global safe_zone

    q = deque()
    visited = set()
    virus = set()

    for i in range(N):
        for j in range(M):
            if board[i][j] != 2: continue
            q.append((i, j))
            visited.add((i, j))
            virus.add((i, j))

    while q:
        ci, cj = q.popleft()
        for di, dj in DIR:
            ni, nj = ci+di, cj+dj
            if not iob(ni, nj): continue
            if (ni, nj) in visited: continue
            if board[ni][nj] == 1: continue
            if (ni, nj) == c1 or (ni, nj) == c2 or (ni, nj) == c3: continue
            virus.add((ni, nj))
            q.append((ni, nj))
            visited.add((ni, nj))

    if virus:
        cnt = 0
        for i in range(N):
            for j in range(M):
                if board[i][j] != 0: continue
                if (i, j) in virus: continue
                if (i, j) == c1 or (i, j) == c2 or (i, j) == c3: continue
                cnt += 1
        safe_zone = max(safe_zone, cnt)


N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
DIR = [(-1,  0), (0, 1), (1, 0), (0, -1)]

candidate = []
safe_zone = -1
for i in range(N):
    for j in range(M):
        if board[i][j] != 0: continue
        candidate.append((i, j))

for i in range(0, len(candidate)-2):
    for j in range(i+1, len(candidate)-1):
        for k in range(j+1, len(candidate)):
            find_safe_zone(candidate[i], candidate[j], candidate[k])
print(safe_zone)