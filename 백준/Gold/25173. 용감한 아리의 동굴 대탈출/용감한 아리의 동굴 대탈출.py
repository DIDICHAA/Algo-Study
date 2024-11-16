from collections import deque


def iob(i, j):
    return 0<=i<N and 0<=j<M


def make_snail(si, sj, d):
    visited = [[False for _ in range(M)] for _ in range(N)]
    visited[si][sj] = True
    lst = []
    length = 1
    i_si, i_sj = si, sj

    while not all(sum(visited, [])):
        for _ in range(2):
            for _ in range(length):
                di, dj = DIR[d]
                ni, nj = si + di, sj + dj
                if iob(ni, nj):
                    visited[ni][nj] = True
                lst.append([ni - i_si, nj - i_sj])
                si, sj = ni, nj
            d = (d + 1) % 4
        length += 1

    return lst


def find_where(number):
    for i in range(N):
        for j in range(M):
            if board[i][j] == number:
                return i, j


def ari_attack():
    global b_health

    b_health -= a_attack
    if b_health <= 0:
        return False
    return True


def ari_move():
    global bef_ai, bef_aj, ai, aj, ad, a_health

    bef_ai, bef_aj = find_where(2)

    di, dj = DIR[ad]
    ni, nj = ai+di, aj+dj
    if iob(ni, nj) and board[ni][nj] == 0:
        ai, aj = ni, nj
        board[bef_ai][bef_aj] = 0
        board[ai][aj] = 2
    else:
        cnt = 0
        while 1:
            if iob(ni, nj) and board[ni][nj] == 0:
                ai, aj = ni, nj
                board[bef_ai][bef_aj] = 0
                board[ai][aj] = 2
                break
            if cnt == 4:
                break
            ad = (ad+1)%4
            di, dj = DIR[ad]
            ni, nj = ai+di, aj+dj
            cnt += 1
            a_health -= 1

    if a_health <= 0:
        return False
    return True


def boss_attack():
    mmi, mmj = find_stone()
    if (mmi, mmj) == (-1, -1):
        return True

    mini_monster(mmi, mmj)

    if a_health <= 0:
        return False
    return True


def find_stone():
    mbi, mbj = find_where(3)
    lst = lst_dict[bd]

    for x, y in lst:
        ni, nj = mbi+x, mbj+y
        if iob(ni, nj) and board[ni][nj] == 1:
            return ni, nj
    return -1, -1


def mini_monster(si, sj):
    global a_health

    q = deque()
    visited = [[False for _ in range(M)] for _ in range(N)]
    q.append((si, sj, b_attack))
    visited[si][sj] = True

    while q:
        ci, cj, mini_attack = q.popleft()
        if (ci, cj) == (ai, aj) and mini_attack > 0:
            a_health -= mini_attack
            return

        for di, dj in DIR:
            ni, nj = ci+di, cj+dj
            if not iob(ni, nj): continue
            if visited[ni][nj]: continue
            if mini_attack == 1: continue
            if (ni, nj) == (bi, bj): continue
            if board[ni][nj] == 1: continue
            visited[ni][nj] = True
            q.append((ni, nj, mini_attack-1))

    return


def boss_move():
    global bi, bj, bd

    if (bef_ai, bef_aj) == (ai, aj):
        return

    board[bi][bj] = 0
    bi, bj = bef_ai, bef_aj
    board[bi][bj] = 3
    bd = ad
    return


N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
a_health, a_attack, b_health, b_attack = map(int, input().split())
DIR = [(-1, 0), (0, 1), (1, 0), (0, -1)]

for i in range(N):
    for j in range(M):
        if board[i][j] == 2:
            ai, aj = i, j
            bef_ai, bef_aj = i, j  # 아리의 이전 위치
        elif board[i][j] == 3:
            bi, bj = i, j

for n in range(4):
    if (ai-bi, aj-bj) == DIR[n]:
        ad, bd = n, n

lst1 = make_snail(0, M-1, 0)
lst2 = make_snail(N-1, M-1, 1)
lst3 = make_snail(N-1, 0, 2)
lst4 = make_snail(0, 0, 3)

lst_dict = {0:lst1, 1:lst2, 2:lst3, 3:lst4}

a_flag = False
num = 1
while 1:
    if not ari_attack():
        a_flag = True
        break
    if not ari_move():
        break
    if not boss_attack():
        break
    boss_move()

if a_flag:
    print('VICTORY!')
else:
    print('CAVELIFE...')