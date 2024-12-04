from collections import deque

def iob(i, j):
    return 0<=i<N and 0<=j<N


def rotate_board(size, s_size):
    for i in range(0, N, size):
        for j in range(0, N, size):
            tmp_board = [lst[j:j+size] for lst in board[i:i+size]]
            tmp_board = list(map(list, zip(*tmp_board[::-1])))

            for k in range(size):
                board[i+k][j:j+size] = tmp_board[k][:]

            # 코드트리 문제에 추가 돼 있는 부분
            # if s_size > 1:
            #     for r in range(0, size, s_size):
            #         for c in range(0, size, s_size):
            #             ttmp_board = [lst[c:c+s_size] for lst in tmp_board[r:r+s_size]]
            #             ttmp_board = list(map(list, zip(*ttmp_board)))[::-1]
            #
            #             for k in range(s_size):
            #                 tmp_board[r+k][c:c+s_size] = ttmp_board[k][:]
            #
            #     for k in range(size):
            #         board[i+k][j:j+size] = tmp_board[k][:]
    return


def melt_ice():
    global board

    melt_board = [lst[:] for lst in board]
    for i in range(N):
        for j in range(N):
            if board[i][j] == 0: continue
            cnt = 0
            for di, dj in DIR:
                ni, nj = i+di, j+dj
                if not iob(ni, nj): continue
                if board[ni][nj] == 0: continue
                cnt += 1

            if cnt < 3:
                melt_board[i][j] -= 1

    board = melt_board
    return


def bfs(si, sj):
    q = deque()
    q.append((si, sj))
    visited.add((si, sj))
    cnt = 1

    while q:
        ci, cj = q.popleft()
        for di, dj in DIR:
            ni, nj = ci+di, cj+dj
            if not iob(ni, nj): continue
            if (ni, nj) in visited: continue
            if board[ni][nj] == 0: continue
            q.append((ni, nj))
            visited.add((ni, nj))
            cnt += 1

    return cnt


N, Q = map(int, input().split())
N = 2**N
board = [list(map(int, input().split())) for _ in range(N)]
levels = list(map(int, input().split()))
DIR = [(-1, 0), (0, 1), (1, 0), (0, -1)]

for level in levels:
    if level != 0:
        rotate_board(2**level, 2**(level-1))
    melt_ice()

max_total = 0
visited = set()
for i in range(N):
    for j in range(N):
        if board[i][j] == 0: continue
        if (i, j) in visited: continue
        ice_cnt = bfs(i, j)
        max_total = max(max_total, ice_cnt)

print(sum(sum(board, [])), max_total, sep='\n')