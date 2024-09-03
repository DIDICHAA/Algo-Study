def oob(i, j):
    return i%N, j%N


# 질량이 0일 때 소멸시키는 함수
# def check_measure():
#     global grid
#     fake_grid = [[[] for _ in range(N)] for _ in range(N)]
#
#     for i in range(N):
#         for j in range(N):
#             for k in range(len(grid[i][j])):
#                 if grid[i][j][k][2] > 0:
#                     fake_grid[i][j].append(grid[i][j][k])
#     grid = fake_grid
#     return
#

# 파이어볼을 합쳤다가 나누고, 새로운 질량과 속력을 부여할 함수
def divide_fireball(d_lst):
    global grid

    mea, spe = 0, 0
    i, j, m, s, d = 0, 0, 0, 0, 0
    num = len(d_lst)
    # if num == 0:
    #     return

    even, odd = 0, 0
    for n in range(len(d_lst)):
        i, j, m, s, d = d_lst[n]
        mea += m  # 총 질량의 합
        spe += s  # 총 속력의 합

        if d % 2 == 0:
            even += 1
        else:
            odd += 1

    # 나누어질 파이어볼에 할당할 질량과 속도, 방향
    m = mea // 5
    s = spe // num

    grid[i][j] = []
    if m > 0:
        if even == 0 or odd == 0:  # 모두 홀수이거나 모두 짝수일 때
            directions = [0, 2, 4, 6]
        else:
            directions = [1, 3, 5, 7]

        for d in directions:
            grid[i][j].append((i, j, m, s, d))

    #check_measure()
    return


def move_fireball():
    global grid

    # 각각 찢어서 넣어놨던 애들을 한 번에 다 이동 시켜야 함
    tmp = [[[] for _ in range(N)] for _ in range(N)]
    for i in range(N):
        for j in range(N):
            for k in range(len(grid[i][j])):
                si, sj = grid[i][j][k][0], grid[i][j][k][1]

                m = grid[i][j][k][2]
                s = grid[i][j][k][3]
                d = grid[i][j][k][4]

                di, dj = dir[d]
                ni, nj = si + di * s, sj + dj * s  # 파이어볼이 이동할 방향

                ni, nj = oob(ni, nj)
                tmp[ni][nj].append((ni, nj, m, s, d))  # 해당 위치에 파이어볼 하나 추가

    grid = tmp

    for i in range(N):
        for j in range(N):
            if len(grid[i][j]) >= 2:  # 파이어볼이 2개 이상일 때
                divide_fireball(grid[i][j])
                # break
    return


N, M, K = map(int, input().split())
grid = [[[] for _ in range(N)] for _ in range(N)]
dir = [(-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1)]  # 0~7번에 해당하는 좌표

for i in range(M):
    r, c, m, s, d = map(int, input().split())  # 문제에서는 좌표가 1부터 시작해서
    grid[r-1][c-1].append((r-1, c-1, m, s, d))


step = 0
while K > 0:
    move_fireball()
    K -= 1

total = 0
for i in range(N):
    for j in range(N):
        for k in range(len(grid[i][j])):
            total += grid[i][j][k][2]

print(total)