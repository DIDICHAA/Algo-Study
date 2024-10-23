def noob(i, j):
    return 0<=i<R and 0<=j<C

def bfs(si, sj):
    global ans

    q = set()
    q.add((si, sj, board[si][sj]))
    while q:
        ci, cj, lst = q.pop()
        for di, dj in DIR:
            ni, nj = ci+di, cj+dj
            if noob(ni, nj) and board[ni][nj] not in lst:
                q.add((ni, nj, lst+board[ni][nj]))
                ans = max(ans, len(lst)+1)


R, C = map(int, input().split())
board = [list(map(str, input().strip())) for _ in range(R)]
DIR = [(-1, 0), (0, 1), (1, 0), (0, -1)]
ans = 1
bfs(0, 0)
print(ans)