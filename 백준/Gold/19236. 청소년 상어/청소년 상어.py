'''
1. 한 칸에ㄴ느 물고기 한 마리가 존재. 1 ~16번 까지의 물고기가 있음

1. 청소년 상어는 (0, 0)에 있는 물고리를 먹고, 그 칸에 들어가게 됨.
    - 상어의 방향은 (0, 0)에 있던 물고기의 방향과 같음. 이후 물고기 이동

2. 물고기 이동 // 단순 구현
    - 번호가 작은 순서부터 차례로 이동. 한 칸씩 이동할 수 있으며
    - 이동할 수 있는 칸은 빈 칸, 다른 물고기가 있는 칸
        - 다른 물고기가 있는 칸이면 서로의 위치를 바꿔주기
    - 이동할 수 없는 칸은 상어가 있는 칸, oob인 칸
    - 만약 이동할 수 있는 칸이 없으면 이동하지 않음.

3. 상어 이동 // 백트래킹
    - 상어는 방향에 있는 칸으로 이동 가능, 한 번에 여러 개의 칸 이동
    - 물고기가 있는 칸으로 이동 시,
        - 그 칸의 물고기를 먹고 그 칸의 방향을 가지게 됨
        - 이동하는 경로에 있는 물고기는 먹지 않음
    - 물고기가 없는 칸으로는 이동 불가
    - 이동 가능한 칸이 없으면 공간에서 벗어나 집으로 감
'''

def noob(i, j):
    return 0<=i<4 and 0<=j<4


def move_fish(sea, fish):
    tmp = [lst[:] for lst in sea]
    tmp_fish = [lst[:] for lst in fish]
    for n in range(1, 17):
        if tmp_fish[n]:
            i, j = tmp_fish[n][0], tmp_fish[n][1]
            d = tmp_fish[n][2]
            di, dj = DIR[d]
            ni, nj = i+di, j+dj
            if noob(ni, nj) and tmp[ni][nj] != -1:
                if tmp[ni][nj] == 0:  # 빈 칸일 때
                    tmp_fish[n] = [ni, nj, d]
                    tmp[ni][nj] = n
                    tmp[i][j] = 0
                else:  # 다른 물고기가 있을 때
                    ano_fish = tmp[ni][nj]
                    tmp_fish[n] = [ni, nj, d]
                    tmp_fish[ano_fish][0], tmp_fish[ano_fish][1] = i, j
                    tmp[i][j], tmp[ni][nj] = tmp[ni][nj], tmp[i][j]

            else:
                cnt = 0
                while 1:
                    if noob(ni, nj) and tmp[ni][nj] != -1:
                        break
                    if cnt == 8:
                        break
                    d = (d+1)%8
                    di, dj = DIR[d]
                    ni, nj = i+di, j+dj
                    cnt += 1
                if cnt != 8:
                    if tmp[ni][nj] == 0:
                        tmp_fish[n] = [ni, nj, d]
                        tmp[ni][nj] = n
                        tmp[i][j] = 0
                    else:
                        ano_fish = tmp[ni][nj]
                        tmp_fish[n] = [ni, nj, d]
                        tmp_fish[ano_fish][0], tmp_fish[ano_fish][1] = i, j
                        tmp[i][j], tmp[ni][nj] = tmp[ni][nj], tmp[i][j]
    return tmp, tmp_fish


def move_shark(res, arr, shark, fish, ni, nj):
    tmp = [lst[:] for lst in arr]
    tmp_shark = shark[:]
    tmp_fish = [lst[:] for lst in fish]

    sx, sy = tmp_shark[0], tmp_shark[1]
    if noob(ni, nj) and tmp[ni][nj] != 0:  # iob고 물고기가 있을 때
        num = tmp[ni][nj]
        res += num
        tmp_shark = [ni, nj, tmp_fish[num][2]]
        tmp_fish[num] = []
        tmp[sx][sy] = 0
        tmp[ni][nj] = -1

    return tmp, tmp_shark, tmp_fish, res


def dfs(res, arr, fish, shark):
    global total

    sx, sy, sd = shark
    di, dj = DIR[sd]
    cnt = 0
    tmp_arr = [lst[:] for lst in arr]
    tmp_info = [lst[:] for lst in fish]
    tmp_shark = shark[:]

    for mul in range(1, 4):
        ni, nj = sx+di*mul, sy+dj*mul
        if noob(ni, nj) and arr[ni][nj] != 0 and arr[ni][nj] != -1:  # oob가 아니고 물고기가 있는 칸만
            new_arr, new_shark, renew_info, tot = move_shark(res, tmp_arr, tmp_shark, tmp_info, ni, nj)
            new_arr, renew_info = move_fish(new_arr, renew_info)
            dfs(tot, new_arr, renew_info, new_shark)
            arr = tmp_arr
            fish = tmp_info
            shark = tmp_shark
        else:
            cnt += 1
    if cnt == 3:  # 이동 못할 때 return 처리 해주기
        total = max(total, res)
        return


sea = [[0 for _ in range(4)] for _ in range(4)]
DIR = [(-1, 0), (-1, -1), (0, -1), (1, -1), (1, 0), (1, 1), (0, 1), (-1, 1)]
fish = [[] for _ in range(17)]
i, j = 0, 0
total = 0  # 최종 출력 변수
for _ in range(4):
    a, b, c, d, e, f, g, h = map(int, input().split())
    fish[a] = [i, j, b-1]
    fish[c] = [i, j+1, d-1]
    fish[e] = [i, j+2, f-1]
    fish[g] = [i, j+3, h-1]
    sea[i][j] = a
    sea[i][j+1] = c
    sea[i][j+2] = e
    sea[i][j+3] = g
    i += 1

# 상어의 시작 위치와, 시작 지점에 있는 물고기 먹고 시작해줌
shark = [0, 0, fish[sea[0][0]][2]]
fish[sea[0][0]] = []
total += sea[0][0]
sea[0][0] = -1  # 상어는 -1로 표시해주기

# 물고기 한 번 이동한 뒤, 상어가 움직이는 것부터 케이스가 갈리니까
# 초기 물고기 이동은 메인에서 함수 돌려주고, 상어가 움직이는 것부터는 dfs 안에서 돌려주기

sea, fish = move_fish(sea, fish)
dfs(total, sea, fish, shark)
print(total)