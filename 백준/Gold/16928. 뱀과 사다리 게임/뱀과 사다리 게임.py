from collections import deque

def bfs():
    q = deque()
    q.append(1)
    visited[1] = True

    while q:
        c = q.popleft()
        for dice in range(1, 7):
            n = c+dice
            if 0 < n <= 100 and not visited[n]:
                if n in ladder.keys():
                    n = ladder[n]
                if n in snake.keys():
                    n = snake[n]
                if not visited[n]:
                    q.append(n)
                    visited[n] = True
                    cnt[n] = cnt[c] + 1


N, M = map(int, input().split())
cnt = [0] * 101
visited = [False] * 101

ladder = dict()
snake = dict()

for _ in range(N):
    x, y = map(int, input().split())
    ladder[x] = y
for _ in range(M):
    x, y = map(int, input().split())
    snake[x] = y

bfs()
print(cnt[100])