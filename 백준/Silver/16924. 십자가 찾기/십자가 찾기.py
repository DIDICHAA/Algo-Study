def check_cross(jaga):
    ans = []
    visited = [[False] * M for _ in range(N)]

    for i in range(1, N-1):
        for j in range(1, M-1):
            if jaga[i][j] == '*':
                k = float('inf')

                for di, dj in dir:
                    mul = 0
                    while 1:
                        ni, nj = i + di*(mul+1), j + dj*(mul+1)
                        if 0<=ni<N and 0<=nj<M and jaga[ni][nj] == '*':
                            mul += 1
                        else: break
                    k = min(k, mul)

                for n in range(1, k+1):
                    ans.append((i+1, j+1, n))
                    visited[i][j] = True

                    for mul in range(1, n+1):
                        for di, dj in dir:
                            ni, nj = i+di*mul, j+dj*mul
                            visited[ni][nj] = True

    for i in range(N):
        for j in range(M):
            if jaga[i][j] == '*' and not visited[i][j]:  # *이 있는 부분부터 십자가가 완성 가능한지 탐색
                return -1, []

    return len(ans), ans


N, M = map(int, input().split())
jaga = [input().strip() for _ in range(N)]
dir = [(0, 1), (0, -1), (1, 0), (-1, 0)]  # 십자가가 뻗어나갈 방향

cnt, crosses = check_cross(jaga)

if cnt == -1:
    print(-1)
else:
    print(cnt)
    for cross in crosses:
        print(cross[0], cross[1], cross[2])
