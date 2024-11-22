from collections import deque

def iob(i, j):
    return 0<=i<N and 0<=j<M


def bfs(si, sj):
    q = deque()
    visited = [[set() for _ in range(M)] for _ in range(N)]
    q.append((si, sj, '', 0))

    while q:
        ci, cj, keys, cnt = q.popleft()

        for di, dj in DIR:
            ni, nj = ci+di, cj+dj
            if not iob(ni, nj): continue
            if board[ni][nj] == '#': continue
            if keys in visited[ni][nj]: continue

            # if toward is key
            if board[ni][nj] in key_candi:
                if board[ni][nj] not in keys:
                    new_keys = keys + board[ni][nj]
                    visited[ni][nj].add(new_keys)
                    q.append((ni, nj, new_keys, cnt+1))
                else:
                    visited[ni][nj].add(keys)
                    q.append((ni, nj, keys, cnt+1))

            # if toward is door
            elif board[ni][nj] in door_candi:
                if board[ni][nj].lower() in keys:
                    q.append((ni, nj, keys, cnt+1))
                    visited[ni][nj].add(keys)

            # if toward is ground
            elif board[ni][nj] == '.':
                q.append((ni, nj, keys, cnt+1))
                visited[ni][nj].add(keys)

            # if toward is exit
            elif board[ni][nj] == '1':
                return cnt+1

    return -1


N, M = map(int, input().split())
board = [list(map(str, input())) for _ in range(N)]
DIR = [(-1, 0), (0, 1), (1, 0), (0, -1)]
key_candi = 'abcdef'
door_candi = 'ABCDEF'
si, sj = 0, 0
for i in range(N):
    for j in range(M):
        if board[i][j] == '0':
            board[i][j] = '.'
            si, sj = i, j

print(bfs(si, sj))