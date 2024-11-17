from collections import deque

def iob(i, j):
    return 0<=i<N and 0<=j<M

def bfs():
    global already

    q = deque()

    for x, y in sset:
        q.append((x, y))
        visited[x][y] = True
        is_open[x][y] = True

    while q:
        ci, cj = q.popleft()
        for di, dj in DIR:
            ni, nj = ci+di, cj+dj
            if not iob(ni, nj): continue
            if board[ni][nj] == '*': continue
            if visited[ni][nj]: continue

            # if face doors
            if board[ni][nj] in door_candi:
                if board[ni][nj].lower() in already:
                    is_open[ni][nj] = True
                    q.append((ni, nj))
                    visited[ni][nj] = True

                # and do not have ones
                else:
                    visited[ni][nj] = True

            # if face keys
            if board[ni][nj] in key_candi:
                is_open[ni][nj] = True
                visited[ni][nj] = True
                already += board[ni][nj]

                # check all the visited doors but not opened
                for i, j in doors:
                    if not visited[i][j]: continue
                    if is_open[i][j]: continue
                    if board[i][j].lower() in already:
                        is_open[i][j] = True
                        q.append((i, j))

                q.append((ni, nj))

            # if face file or ground
            if board[ni][nj] == '$' or board[ni][nj] == '.':
                is_open[ni][nj] = True
                visited[ni][nj] = True
                q.append((ni, nj))

    cnt = 0
    for i in range(N):
        for j in range(M):
            if board[i][j] != '$': continue
            if not is_open[i][j]: continue
            cnt += 1
    return cnt


T = int(input())
for tc in range(T):
    N, M = map(int, input().split())
    board = [list(map(str, input())) for _ in range(N)]
    already = input()
    DIR = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    key_candi = 'abcdefghijklmnopqrstuvwxyz'
    door_candi = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

    doors = []
    is_open = [[False for _ in range(M)] for _ in range(N)]
    visited = [[False for _ in range(M)] for _ in range(N)]

    sset = set()

    for i in range(N):
        if board[i][0] == '$':
            sset.add((i, 0))
        elif board[i][0] == '.':
            sset.add((i, 0))
        elif board[i][0] in door_candi:
            if board[i][0].lower() in already:
                sset.add((i, 0))
            else:
                visited[i][0] = True
        elif board[i][0] in key_candi and board[i][0] not in already:
            already += board[i][0]
            sset.add((i, 0))

        if board[i][M-1] == '$':
            sset.add((i, M-1))
        elif board[i][M-1] == '.':
            sset.add((i, M-1))
        elif board[i][M-1] in door_candi:
            if board[i][M-1].lower() in already:
                sset.add((i, M-1))
            else:
                visited[i][M-1] = True
        elif board[i][M-1] in key_candi and board[i][M-1] not in already:
            already += board[i][M-1]
            sset.add((i, M-1))

    for j in range(M):
        if board[0][j] == '$':
            sset.add((0, j))
        elif board[0][j] == '.':
            sset.add((0, j))
        elif board[0][j] in door_candi:
            if board[0][j].lower() in already:
                sset.add((0, j))
            else:
                visited[0][j] = True
        elif board[0][j] in key_candi and board[0][j] not in already:
            already += board[0][j]
            sset.add((0, j))

        if board[N-1][j] == '$':
            sset.add((N-1, j))
        elif board[N-1][j] == '.':
            sset.add((N-1, j))
        elif board[N-1][j] in door_candi:
            if board[N-1][j].lower() in already:
                sset.add((N-1, j))
            else:
                visited[N-1][j] = True
        elif board[N-1][j] in key_candi and board[N-1][j] not in already:
            already += board[N-1][j]
            sset.add((N-1, j))

    for i in range(N):
        for j in range(M):
            if board[i][j] in door_candi:
                doors.append([i, j])

    print(bfs())