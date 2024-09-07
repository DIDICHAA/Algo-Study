from collections import deque

def meet_juye(s, e):
    q = deque()
    visited[s] = 1
    q.append(s)

    while q:
        c = q.popleft()
        if c == e:
            return visited[c] - 1

        for n in adj[c]:
            if visited[n] == 0:
                visited[n] = visited[c] + 1
                q.append(n)


N, M = map(int, input().split())
S, E = map(int, input().split())
adj = [[] for _ in range(N+1)]
visited = [0]*(N+1)

for _ in range(M):
    s, e = map(int, input().split())
    adj[s].append(e)
    adj[e].append(s)

for i in range(1, len(adj)):
    if i+1 < len(adj):
        adj[i].append(i+1)
    adj[i].append(i-1)

ans = meet_juye(S, E)
print(ans)