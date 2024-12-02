def iob(i, j):
    return 0<=i<N and 0<=j<M


def calcul(lst):
    global ans

    if N > M:
        t = N
    else:
        t = M

    arr = [row[:] for row in board]
    for i in range(len(candidate)):
        directions = lst[i]
        x, y = grid[i]
        for di, dj in directions:
            for mul in range(1, t):
                ni, nj = x+di*mul, y+dj*mul
                if not iob(ni, nj): continue
                if board[ni][nj] == 6: break
                arr[ni][nj] = '.'

    ans = min(ans, sum(arr, []).count(0))
    return


def dfs(cnt, idx, lst):
    if cnt == len(candidate):
        calcul(lst)
        return

    for i in range(idx, len(candidate)):
        directions = sight_dict[candidate[i]]
        for n in range(len(directions)):
            lst.append(directions[n])
            dfs(cnt+1, i+1, lst)
            lst.pop()


N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
sight_dict = {
    1:[[(-1, 0)], [(0, 1)], [(1, 0)], [(0, -1)]],
    2:[[(0, -1), (0, 1)], [(-1, 0), (1, 0)]],
    3:[[(-1, 0), (0, 1)], [(0, 1), (1, 0)], [(1, 0), (0, -1)], [(0, -1), (-1, 0)]],
    4:[[(-1, 0), (0, 1), (0, -1)], [(-1, 0), (0, 1), (1, 0)], [(0, 1), (1, 0), (0, -1)], [(1, 0), (0, -1), (-1, 0)]],
    5:[[(-1, 0), (0, 1), (1, 0), (0, -1)]]
}
candidate, grid = [], []
for i in range(N):
    for j in range(M):
        if 0 < board[i][j] < 6:
            candidate.append(board[i][j])
            grid.append([i, j])

ans = 1e9
dfs(0, 0, [])

print(ans)