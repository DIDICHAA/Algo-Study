from collections import deque

def iob(i, j):
    return 0<=i<12 and 0<=j<6


def bomb(si, sj, puyo):
    global whole_visited

    q = deque()
    visited = set()
    q.append((si, sj, puyo))
    visited.add((si, sj))
    lst = [(si, sj)]

    while q:
        ci, cj, now = q.popleft()
        for di, dj in DIR:
            ni, nj = ci+di, cj+dj
            if not iob(ni, nj): continue
            if (ni, nj) in visited: continue
            if board[ni][nj] != now: continue
            lst.append((ni, nj))
            visited.add((ni, nj))
            q.append((ni, nj, board[ni][nj]))

    if len(lst) >= 4:
        for x, y in lst:
            board[x][y] = '.'
        return True
    else:
        for x, y in lst:
            whole_visited.add((x, y))
        return False

def fall_down():
    global board

    new_board = [['.' for _ in range(6)] for _ in range(12)]
    tmp = []

    for j in range(6):
        for i in range(12):
            if board[i][j] == '.': continue
            tmp.append(board[i][j])
        if tmp:
            tmp.reverse()
            pi = 11
            for new_puyo in tmp:
                new_board[pi][j] = new_puyo
                pi -= 1
            tmp = []
    board = new_board


board = [list(map(str, input())) for _ in range(12)]
DIR = [(-1, 0), (0, 1), (1, 0), (0, -1)]
time = 0

while 1:
    whole_visited = set()
    flag = False
    for i in range(12):
        for j in range(6):
            if board[i][j] == '.': continue
            if (i, j) in whole_visited: continue
            if bomb(i, j, board[i][j]):
                flag = True

    if flag:
        time += 1
        fall_down()
    else:
        break

print(time)