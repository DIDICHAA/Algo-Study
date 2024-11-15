from collections import deque


def iob(i, j):
    return 0<=i<R and 0<=j<C


def check():
    for x, y in candidate:
        if temp[x][y] < K:
            return False
    return True


def check_cannot(hd, d, i, j):
    if d == 0:
        if cannot_go[i][j][hd]:
            return False
        return True

    elif d == 1 or d == 3:
        di, dj = DIR[(hd+2)%4]
        if cannot_go[i][j][hd] or cannot_go[i+di][j+dj][(hd+d)%4]:
            return False
        return True


def blow():
    for hi, hj, hd in heater:
        q = deque()
        tmp_temp = [[0 for _ in range(C)] for _ in range(R)]

        d1, n1, d2, n2, num = 0, 1, 0, 0, 5
        di1, dj1 = DIR[(hd+d1)%4]
        di2, dj2 = DIR[(hd+d2)%4]
        ni, nj = hi + (di1*n1) + (di2*n2), hj + (dj1*n1) + (dj2*n2)
        q.append((ni, nj, 5, 0))

        while q:
            ci, cj, num, d = q.popleft()
            if num == 0: continue
            if not iob(ci, cj): continue
            if tmp_temp[ci][cj] != 0: continue
            if not check_cannot(hd, d, ci, cj): continue
            tmp_temp[ci][cj] += num
            for di, dj, nd in DIR_CHECK[hd]:
                q.append((ci+di, cj+dj, num-1, nd))

        for i in range(R):
            for j in range(C):
                temp[i][j] += tmp_temp[i][j]
    return


def control():
    global temp

    tmp_board = [lst[:] for lst in temp]
    visited = [[[False for _ in range(4)] for _ in range(C)] for _ in range(R)]

    for i in range(R):
        for j in range(C):
            if temp[i][j] == 0: continue
            now_temp = temp[i][j]
            for d in range(4):
                di, dj = DIR[d]
                ni, nj = i+di, j+dj
                if not iob(ni, nj): continue
                if cannot_go[ni][nj][d]: continue
                if visited[i][j][d] or visited[ni][nj][(d+2)%4]: continue
                visited[i][j][d], visited[ni][nj][(d+2)%4] = True, True
                c_temp = abs(now_temp - temp[ni][nj]) // 4
                if now_temp > temp[ni][nj]:
                    tmp_board[ni][nj] += c_temp
                    tmp_board[i][j] -= c_temp
                else:
                    tmp_board[ni][nj] -= c_temp
                    tmp_board[i][j] += c_temp

    temp = tmp_board
    return


def decrease():
    for i in range(1, R-1):
        if temp[i][0] > 0:
            temp[i][0] -= 1
        if temp[i][C-1] > 0:
            temp[i][C-1] -= 1

    for j in range(1, C-1):
        if temp[0][j] > 0:
            temp[0][j] -= 1
        if temp[R-1][j] > 0:
            temp[R-1][j] -= 1

    for x, y in ((0, 0), (0, C-1), (R-1, 0), (R-1, C-1)):
        if temp[x][y] > 0:
            temp[x][y] -= 1
    return


R, C, K = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(R)]
temp = [[0 for _ in range(C)] for _ in range(R)]
cannot_go = [[[False for _ in range(4)] for _ in range(C)] for _ in range(R)]
W = int(input())

for _ in range(W):
    x, y, t = map(lambda n:int(n)-1, input().split())
    if t == -1:
        cannot_go[x][y][1] = True
        if iob(x-1, y):
            cannot_go[x-1][y][3] = True
    else:
        cannot_go[x][y][2] = True
        if iob(x, y+1):
            cannot_go[x][y+1][0] = True

DIR_CHECK = [
    [(-1, 1, 3), (0, 1, 0), (1, 1, 1)],
    [(1, -1, 1), (1, 0, 0), (1, 1, 3)],
    [(-1, -1, 1), (0, -1, 0), (1, -1, 3)],
    [(-1, -1, 3), (-1, 0, 0), (-1, 1, 1)]
]
DIR = [(0, 1), (1, 0), (0, -1), (-1, 0)]
DIR_MAP = [None, 0, 2, 3, 1]

candidate, heater = [], []
for i in range(R):
    for j in range(C):
        if board[i][j] == 5:
            candidate.append([i, j])
        elif board[i][j] > 0:
            heater.append([i, j, DIR_MAP[board[i][j]]])

for chocolate in range(1, 102):
    blow()
    control()
    decrease()
    if check():
        break

print(chocolate)