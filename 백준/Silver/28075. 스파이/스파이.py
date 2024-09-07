def dfs(d, pre, total):
    global result

    if d == N + 1:
        if total >= M:
            result += 1
        return

    for work in range(2):
        for place in range(3):
            if place == pre:
                dfs(d + 1, place, total + mission[work][place] // 2)
            else:
                dfs(d + 1, place, total + mission[work][place])


N, M = map(int, input().split())
mission = [list(map(int, input().split())) for _ in range(2)]
result = 0

dfs(1, -1, 0)
print(result)