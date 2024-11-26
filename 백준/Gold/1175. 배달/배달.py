from collections import deque


def iob(i, j):
    return 0<=i<N and 0<=j<M


def bfs(si, sj):
    q = deque()
    visited = [[[False for _ in range(4)] for _ in range(M)] for _ in range(N)]
    q.append((si, sj, -1, []))
    cnts = [[0 for _ in range(M)] for _ in range(N)]

    while q:
        ci, cj, cd, lst = q.popleft()

        for d in range(4):
            if d == cd: continue
            di, dj = DIR[d]
            ni, nj = ci+di, cj+dj
            if not iob(ni, nj): continue
            if visited[ni][nj][d]: continue
            if board[ni][nj] == '#': continue

            if board[ni][nj] == 'C':
                if len(lst) == 1 and [ni, nj] not in lst:
                    return cnts[ci][cj] + 1

                elif not lst:
                    q.clear()
                    visited = [[[False for _ in range(4)] for _ in range(M)] for _ in range(N)]
                    visited[ni][nj][d] = True
                    for dd in range(4):
                        ddi, ddj = DIR[dd]
                        nni, nnj = ni+ddi, nj+ddj
                        if not iob(nni, nnj): continue
                        if (dd+2)%4 == d: continue
                        if cnts[nni][nnj] != 0 and cnts[nni][nnj] == cnts[ci][cj]:
                            q.append((ni, nj, (dd+2)%4, lst+[[ni, nj]]))
                            visited[ni][nj][(dd+2)%4] = True
                    q.append((ni, nj, d, lst+[[ni, nj]]))
                    cnts[ni][nj] = cnts[ci][cj] + 1
                    board[ni][nj] = '.'
                    break

            else:
                q.append((ni, nj, d, lst))
                visited[ni][nj][d] = True
                cnts[ni][nj] = cnts[ci][cj] + 1
    return -1


N, M = map(int, input().split())
board = [list(map(str, input())) for _ in range(N)]
DIR = [(-1, 0), (0, 1), (1, 0), (0, -1)]

for i in range(N):
    for j in range(M):
        if board[i][j] == 'S':
            board[i][j] = '.'
            si, sj = i, j
print(bfs(si, sj))