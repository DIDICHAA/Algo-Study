# A의 각각의 군집과 B의 각각의 군집이 동일한 좌표, 동일한 사이즈 여야 함
from collections import deque

def iob(i, j):
    return 0<=i<N and 0<=j<M


def check_poss(check_a, color):
    for x, y in check_a:
        if flag_b[x][y] != color:
            return False
        else: continue
    return True


def figure(x, y):
    q = deque()
    visited_a = set()
    q.append((x, y))
    visited_a.add((x, y))

    while q:
        ci, cj = q.popleft()
        for di, dj in DIR:
            ni, nj = ci+di, cj+dj
            if not iob(ni, nj): continue
            if (ni, nj) in visited_a: continue
            if flag_a[ci][cj] != flag_a[ni][nj] : continue
            visited_a.add((ni, nj))
            visited[ni][nj] = True
            q.append((ni, nj))
    col = flag_b[x][y]

    if check_poss(visited_a, col):
        return True
    else:
        return False


N, M = map(int, input().split())
flag_a = [list(map(str, input())) for _ in range(N)]
flag_b = [list(map(str, input())) for _ in range(N)]
DIR = [(-1, 0), (0, 1), (1, 0), (0, -1)]

visited = [[False for _ in range(M)] for _ in range(N)]
flag = True

for i in range(N):
    for j in range(M):
        if visited[i][j]: continue
        visited[i][j] = True
        # 해당 군집이 flag_b와 동일할 때
        if figure(i, j): continue
        else: flag = False

if flag:
    print('YES')
else:
    print('NO')