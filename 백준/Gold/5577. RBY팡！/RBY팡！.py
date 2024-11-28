def change(t):

    left, right = t, t
    size = -1
    total = 0

    while 0 <= left and right < N:
        if balls[left] != balls[right]: break

        color = balls[left]

        while 0 <= left and balls[left] == color:
            left -= 1
            size += 1

        while right < N and balls[right] == color:
            right += 1
            size += 1

        if size < 4: break
        total += size
        size = 0

    return N - total


N = int(input())
balls = []
for _ in range(N):
    balls.append(int(input()))

if N < 4:
    print(N)
else:
    candidate = [1, 2, 3]
    ans = 1e9
    for n in range(N):
        target = balls[n]
        for next in range(1, 4):
            if next == target: continue
            balls[n] = next
            ans = min(ans, change(n))
            balls[n] = target
    print(ans)