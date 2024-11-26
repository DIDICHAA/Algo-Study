from collections import deque


def iob(i, j):
    return 0<=i<N and 0<=j<M

# find island cluster
def find_island(si, sj):
    q = deque()
    q.append((si, sj))
    checked[si][sj] = True
    island[si][sj] = num

    while q:
        ci, cj = q.popleft()
        for di, dj in DIR:
            ni, nj = ci+di, cj+dj
            if not iob(ni, nj): continue
            if checked[ni][nj]: continue
            if board[ni][nj] == 0: continue

            checked[ni][nj] = True
            island[ni][nj] = num
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


# finally check if this combination could connect all islands
def check_island(bridge_lst):
    global total_length

    arr = [[set() for _ in range(M)] for _ in range(N)]
    q = deque()
    visited = set()
    tmp_length = 0
    for num1, num2, lst in bridge_lst:
        for x, y in lst:
            arr[x][y].add(num1)
            arr[x][y].add(num2)
        tmp_length += len(lst)

    num_set = set()
    for x, y in start:
        q.append((x, y))
        visited.add((x, y))
    num_set.add(1)

    while q:
        ci, cj = q.popleft()
        for di, dj in DIR:
            ni, nj = ci+di, cj+dj
            if not iob(ni, nj): continue
            if (ni, nj) in visited: continue

            # if toward is bridge
            if island[ci][cj] > 0 and island[ci][cj] in arr[ni][nj]:
                q.append((ni, nj))
                visited.add((ni, nj))

            # from bridge
            elif island[ci][cj] == 0:
                # to bridge
                if island[ni][nj] == 0:
                    for n in arr[ci][cj]:
                        if n not in arr[ni][nj]: continue
                        q.append((ni, nj))
                        visited.add((ni, nj))
                # to island
                elif island[ni][nj] > 0:
                    if island[ni][nj] in arr[ci][cj]:
                        q.append((ni, nj))
                        visited.add((ni, nj))
                        num_set.add(island[ni][nj])

            elif island[ci][cj] > 0 and island[ni][nj] == island[ci][cj]:
                q.append((ni, nj))
                visited.add((ni, nj))

    if len(num_set) == num:
        total_length = min(total_length, tmp_length)
    return


# make bridge combinations
def make_comb(cnt, idx, max_cnt, lst):
    if cnt == max_cnt:
        check_island(lst)
        return

    for i in range(idx, len(route_comb_lst)):
        lst.append(route_comb_lst[i])
        make_comb(cnt+1, i+1, max_cnt, lst)
        lst.pop()


N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
island = [[0 for _ in range(M)] for _ in range(N)]
DIR = [(-1, 0), (0, 1), (1, 0), (0, -1)]

num = 1
checked = [[False for _ in range(M)] for _ in range(N)]
for i in range(N):
    for j in range(M):
        if checked[i][j]: continue
        if board[i][j] != 1: continue
        find_island(i, j)
        num += 1

num -= 1
start = []
for i in range(N):
    for j in range(M):
        if island[i][j] == 1:
            start.append([i, j])

total_length = 1e9
route_comb_lst = []
for i in range(1, num):
    for j in range(i+1, num+1):
        flag, route = make_bridge(i, j)
        if flag:
            route_comb_lst.append([i, j, route])

for n in range(num-1, num+1):
    make_comb(0, 0, n, [])

if total_length == 1e9:
    print(-1)
else:
    print(total_length)