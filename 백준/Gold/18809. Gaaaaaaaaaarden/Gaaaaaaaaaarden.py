def iob(i, j):
    return 0 <= i < N and 0 <= j < M


def bfs(nutri, candi):
    global ans

    arr = [[0 for _ in range(M)] for _ in range(N)]
    q = set()

    for n in range(len(candi)):
        x, y = candi[n]
        arr[x][y] = nutri[n]
        q.add((x, y, nutri[n]))

    while q:
        tq = set()
        for ci, cj, color in q:
            for di, dj in DIR:
                ni, nj = ci + di, cj + dj
                if not iob(ni, nj): continue
                if arr[ni][nj] != 0: continue  # 현재 case에서 이미 빈칸이 아닐 때
                if board[ni][nj] == 0: continue  # 호수일 때

                tq.add((ni, nj, color))

        for x, y, color in tq:
            if arr[x][y] == 0:
                arr[x][y] = color
            else:
                if arr[x][y] != color:
                    arr[x][y] = 7

        ttq = set()
        for x, y, color in tq:
            if arr[x][y] == 7:
                continue
            else:
                ttq.add((x, y, color))

        q = ttq
    ans = max(ans, sum(arr, []).count(7))
    return


def make_candi_c(cnt, idx, lst):
    if cnt == G + R:
        c_lst.append(lst[:])
        return

    for i in range(idx, len(candidate)):
        lst.append(candidate[i])
        make_candi_c(cnt + 1, i + 1, lst)
        lst.pop()


def make_p(cnt, lst):
    if cnt == G + R:
        solve(lst)
        return

    for i in range(2):
        if nutrition[i] <= 0: continue
        nutrition[i] -= 1
        if i == 0:
            lst.append(3)
            make_p(cnt+1, lst)
            lst.pop()
            nutrition[i] += 1
        else:
            lst.append(4)
            make_p(cnt+1, lst)
            lst.pop()
            nutrition[i] += 1


def solve(nutri):
    for candi in c_lst:
        bfs(nutri, candi)
    return


N, M, G, R = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
DIR = [(-1, 0), (0, 1), (1, 0), (0, -1)]
candidate = []
for i in range(N):
    for j in range(M):
        if board[i][j] != 2: continue
        candidate.append([i, j])

nutrition = [G, R]

ans = 0
c_lst = []
make_candi_c(0, 0, [])
make_p(0, [])

print(ans)