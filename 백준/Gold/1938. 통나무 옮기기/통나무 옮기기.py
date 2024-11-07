from collections import deque

def iob(i, j):
    return 0<=i<N and 0<=j<N

# type이 세로일 때
def check(i, j, n):
    if n == 0 or n == 2:
        di, dj = DIR[n]
        ni, nj = i+di, j+dj
        if iob(ni, nj) and board[ni][nj] == 0:
            return True

    elif n == 1 or n == 3:
        ni, nj = i-1, j
        nni, nnj = i+1, j
        if board[ni][nj] == board[nni][nnj] == 0:
            return True

    return False


# type이 가로일 때
def check_2(i, j, n):
    if n == 0 or n == 2:
        ni, nj = i, j-1
        nni, nnj = i, j+1
        if board[ni][nj] == board[nni][nnj] == 0:
            return True

    elif n == 1 or n == 3:
        di, dj = DIR[n]
        ni, nj = i+di, j+dj
        if iob(ni, nj) and board[ni][nj] == 0:
            return True

    return False


def rotate_check(i, j, type):
    cnt = 0
    for di, dj in rot_check:
        ni, nj = i+di, j+dj
        if not iob(ni, nj): continue
        if board[ni][nj] != 0: continue
        cnt += 1
    if cnt == 8:
        if type:
            return True, 0
        else:
            return True, 1
    return False, -1


def bfs(si, sj, type):
    q = deque()
    visited = [[[0]*2 for _ in range(N)] for _ in range(N)]
    q.append((si, sj, type))
    visited[si][sj][type] = 1

    while q:
        ci, cj, type = q.popleft()
        if (ci, cj) == (ei, ej) and type == etype:
            return visited[ci][cj][type]-1

        for i in range(4):
            di, dj = DIR[i]
            ni, nj = ci+di, cj+dj
            if not iob(ni, nj): continue
            if visited[ni][nj][type] != 0: continue
            if board[ni][nj] == 1: continue

            if type:
                if check(ni, nj, i):
                    visited[ni][nj][type] = visited[ci][cj][type] + 1
                    q.append((ni, nj, type))
            else:
                if check_2(ni, nj, i):
                    visited[ni][nj][type] = visited[ci][cj][type] + 1
                    q.append((ni, nj, type))

        flag, ntype = rotate_check(ci, cj, type)
        if flag and visited[ni][nj][ntype] == 0:
            visited[ci][cj][ntype] = visited[ci][cj][type] + 1
            q.append((ci, cj, ntype))

    return 0


N = int(input())
tmp = [list(map(str, input().strip())) for _ in range(N)]
board = [[0 for _ in range(N)] for _ in range(N)]
DIR = [(-1, 0), (0, 1), (1, 0), (0, -1)]
rot_check = [(-1, -1), (-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1)]
ans = 1e9
tree, end = [], []
for i in range(N):
    for j in range(N):
        if tmp[i][j] == 'B':
            board[i][j] = 0
            tree.append((i, j))
        elif tmp[i][j] == '1':
            board[i][j] = 1
        elif tmp[i][j] == 'E':
            end.append((i, j))

ex, ey = end[0]
ei, ej = end[1]
if abs(ex-ei) == 1:
    etype = 1
else:
    etype = 0

x, y = tree[0]
x1, y1 = tree[1]
if abs(x-x1) == 1:
    print(bfs(x1, y1, 1))
else:
    print(bfs(x1, y1, 0))
