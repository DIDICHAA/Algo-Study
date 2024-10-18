N, M = map(int, input().split())
board = [[0 for _ in range(100)] for _ in range(100)]
for _ in range(N):
    x, y, x2, y2 = map(lambda x:int(x)-1, input().split())
    for i in range(x, x2+1):
        for j in range(y, y2+1):
            board[i][j] += 1

cnt = 0
for i in range(100):
    for j in range(100):
        if board[i][j] > M:
            cnt += 1
print(cnt)