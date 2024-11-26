from collections import deque


def iob(i, j):
    return 0<=i<N and 0<=j<M


def bfs(si, sj):
    q = deque()
    visited = [[[0 for _ in range(2)] for _ in range(M)] for _ in range(N)]
    q.append((si, sj, False))
    visited[si][sj][0] = 1

    while q:
        ci, cj, is_have = q.popleft()
        if (ci, cj) == (N-1, M-1):
            if visited[ci][cj][is_have] - 1 <= T:
                return visited[ci][cj][is_have] - 1
            else:
                return 'Fail'

        for di, dj in DIR:
            ni, nj = ci+di, cj+dj
            if not iob(ni, nj): continue
            if visited[ni][nj][is_have] != 0: continue

            if is_have and board[ni][nj] == 1:
                visited[ni][nj][1] = visited[ci][cj][is_have] + 1
                q.append((ni, nj, True))

            elif board[ni][nj] == 2:
                visited[ni][nj][1] = visited[ci][cj][is_have] + 1
                q.append((ni, nj, True))

            elif board[ni][nj] == 0:
                visited[ni][nj][is_have] = visited[ci][cj][is_have] + 1
                q.append((ni, nj, is_have))

    return 'Fail'


N, M, T = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
DIR = [(-1, 0), (0, 1), (1, 0), (0, -1)]

print(bfs(0, 0))