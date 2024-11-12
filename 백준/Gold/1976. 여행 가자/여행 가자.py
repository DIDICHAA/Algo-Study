def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]


def union(a, b):
    a = find(a)
    b = find(b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

    return


N = int(input())
M = int(input())
parent = [i for i in range(N)]

for i in range(N):
    lst = list(map(int, input().split()))
    for j in range(N):
        if lst[j] == 1:
            union(i, j)

parent = [-1] + parent
plan = list(map(int, input().split()))
s = parent[plan[0]]
flag = True
for i in range(1, M):
    if parent[plan[i]] != s:
        flag = False
        break

if flag:
    print("YES")
else:
    print("NO")