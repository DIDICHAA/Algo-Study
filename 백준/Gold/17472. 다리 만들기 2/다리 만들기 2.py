from collections import deque


def iob(i, j):
    return 0<=i<N and 0<=j<M


# find island cluster
def find_island(si, sj):
    q = deque()
    q.append((si, sj))
    checked[si][sj] = True

    while q:
        ci, cj = q.popleft()
        island[ci][cj] = num
        for di, dj in DIR:
            ni, nj = ci+di, cj+dj
            if not iob(ni, nj): continue
            if checked[ni][nj]: continue
            if board[ni][nj] == 0: continue

            checked[ni][nj] = True
            q.append((ni, nj))


# make the shortest bridge between two islands
def make_bridge(num1, num2):
    q = deque()

    for i in range(N):
        for j in range(M):
            if island[i][j] != num1: continue
            for n in range(4):
                q.append((i, j, n, []))

    while q:
        ci, cj, cd, route = q.popleft()
        di, dj = DIR[cd]
        ni, nj = ci+di, cj+dj
        if not iob(ni, nj): continue
        if island[ni][nj] == num1: continue

        if island[ni][nj] == 0:
            q.append((ni, nj, cd, route+[[ni, nj]]))

        elif island[ni][nj] == num2:
            if len(route) < 2: continue
            return True, route

    return False, []


def find(x):
    if parents[x] != x:
        parents[x] = find(parents[x])
    return parents[x]


def union(i, j):
    ti, tj = find(i), find(j)
    if ti != tj:
        if ti > tj:
            parents[ti] = tj
        else:
            parents[tj] = ti


# finally check if this combination could connect all islands
def check_island(bridge_lst):
    global total_length

    original_parents = parents[:]
    flag = True
    temp = 0
    for x, y, bridge in bridge_lst:
        if find(x) != find(y):
            union(x, y)
            temp += len(bridge)
        else:
            flag = False

    if flag:
        total_length = min(total_length, temp)

    parents[:] = original_parents
    return


# make bridge combinations
def make_comb(cnt, idx, lst):
    if cnt == num-1:
        check_island(lst)
        return

    for i in range(idx, len(route_comb_lst)):
        lst.append(route_comb_lst[i])
        make_comb(cnt+1, i+1, lst)
        lst.pop()


N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
island = [[0 for _ in range(M)] for _ in range(N)]
DIR = [(-1, 0), (0, 1), (1, 0), (0, -1)]

num = 0
checked = [[False for _ in range(M)] for _ in range(N)]
for i in range(N):
    for j in range(M):
        if checked[i][j]: continue
        if board[i][j] != 1: continue
        num += 1
        find_island(i, j)

total_length = 1e9
route_comb_lst = []
parents = [i for i in range(num+1)]
for i in range(1, num):
    for j in range(i+1, num+1):
        flag, route = make_bridge(i, j)
        if flag:
            route_comb_lst.append([i, j, route])

make_comb(0, 0, [])

print(total_length if total_length != 1e9 else -1)