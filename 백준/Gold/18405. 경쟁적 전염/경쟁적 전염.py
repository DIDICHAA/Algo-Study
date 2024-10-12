def noob(i, j):
    return 0<=i<N and 0<=j<N

def copied(num):
    tmp = []
    for i in range(N):
        for j in range(N):
            if board[i][j] != num: continue
            for di, dj in DIR:
                ni, nj = i+di, j+dj
                if noob(ni, nj) and board[ni][nj] == 0:
                    tmp.append(([ni, nj, num]))

    for x, y, num in tmp:
        board[x][y] = num

    return


N, K = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
S, X, Y = map(int, input().split())
DIR = [(-1, 0), (0, 1), (1, 0), (0, -1)]
for _ in range(S):
    for num in range(1, K+1):
        copied(num)
    tmp = sum(board, [])
    if tmp.count(0) == 0:
        break
print(board[X-1][Y-1])