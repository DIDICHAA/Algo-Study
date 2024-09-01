T = int(input())

for tc in range(T):
    M, N = map(int, input().split())
    grid = [list(map(int, input().split())) for _ in range(M)]
    real_grid = list(zip(*grid))

    cnt = 0
    for i in range(N):
        bottom = M-1
        for j in range(M-1, -1, -1):
            if real_grid[i][j] == 1:
                cnt += bottom - j
                bottom -= 1
    print(cnt)