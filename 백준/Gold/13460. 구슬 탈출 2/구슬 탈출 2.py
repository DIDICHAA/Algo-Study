def move_gooseul(si, sj, di, dj):
    while board[si][sj] == '.':
        si += di
        sj += dj

    if board[si][sj] == '#':
        si -= di
        sj -= dj

    return si, sj


def dfs(cnt, ri, rj, bi, bj):
    global ans

    if cnt == 10:
        return

    for i in range(4):
        di, dj = DIR[i]
        nri, nrj = move_gooseul(ri, rj, di, dj)
        nbi, nbj = move_gooseul(bi, bj, di, dj)
        if board[nbi][nbj] == 'O': continue

        if (nri, nrj) == (nbi, nbj):
            if i == 0:  # 위로 밀려있을 때
                if ri > bi:
                    nri += 1
                else:
                    nbi += 1
            elif i == 1:  # 우로 밀려있을 때
                if rj > bj:
                    nbj -= 1
                else:
                    nrj -= 1
            elif i == 2:  # 하로 밀려있을 때
                if ri > bi:
                    nbi -= 1
                else:
                    nri -= 1
            else:  # 좌로 밀려있을 때
                if rj > bj:
                    nrj += 1
                else:
                    nbj += 1

        if board[nri][nrj] == 'O':
            ans = min(ans, cnt+1)
            return

        dfs(cnt + 1, nri, nrj, nbi, nbj)


N, M = map(int, input().split())
board = [list(map(str, input().strip())) for _ in range(N)]
DIR = [(-1, 0), (0, 1), (1, 0), (0, -1)]
ans = 100

for i in range(N):
    for j in range(M):
        if board[i][j] == 'R':
            board[i][j] = '.'
            ri, rj = i, j
        elif board[i][j] == 'B':
            board[i][j] = '.'
            bi, bj = i, j

dfs(0, ri, rj, bi, bj)

if ans == 100:
    print(-1)
else:
    print(ans)