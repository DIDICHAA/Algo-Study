def find(x):
    if x != v_lst[x]:
        v_lst[x] = find(v_lst[x])
    return v_lst[x]


def union(x, y):
    if x > y:
        v_lst[x] = y
        return True
    elif x < y:
        v_lst[y] = x
        return True
    return False


N = int(input())
w_cost = []
ans = 0
v_lst = [i for i in range(N+1)]
for i in range(1, N+1):
    w_cost.append([int(input()), 0, i])

for i in range(N):
    tmp_lst = list(map(int, input().split()))
    for j in range(N):
        if i != j:
            w_cost.append([tmp_lst[j], i+1, j+1])

w_cost.sort()
for cost, start, end in w_cost:
    ns = find(start)
    ne = find(end)
    if union(ns, ne):
        ans += cost

print(ans)