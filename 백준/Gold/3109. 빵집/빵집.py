def iob(i, j):
    return 0<=i<R and 0<=j<C


def dfs(si, sj):
    if sj == C-1:
        return True

    for d in range(3):
        di, dj = DIR[d]
        ni, nj = si+di, sj+dj
        if iob(ni, nj) and tmp_board[ni][nj] == '.':
            tmp_board[ni][nj] = 'x'
            if dfs(ni, nj):
                return True
    return False


R, C = map(int, input().split())
board = [list(map(str, input())) for _ in range(R)]
DIR = [(-1, 1), (0, 1), (1, 1)]
ans = 0

tmp_board = [lst[:] for lst in board]
for i in range(R):
    tmp_board[i][0] = 'x'
    if dfs(i, 0):
        ans += 1
print(ans)