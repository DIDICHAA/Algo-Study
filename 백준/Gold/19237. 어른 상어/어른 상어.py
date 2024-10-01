'''
** 문제에서 요구하는 순서대로 구현하기 **
** 빈 queue나 list 없는 지 확인하기 **
** 2-2번 잘 확인하기 **

1413 문제 이해
- 상어에는 1 ~ M번의 자연수, 모든 번호는 다름
- 1번 상어가 제일 셈

1. 맨 처음 각 상어가 자신의 위치에 자신의 냄새를 뿌림
2. 그 후 1초마다 모든 상어가 동시에 상하좌우로 인접한 칸 중 하나로 이동
    -> 그 칸에다가 자신의 냄새를 뿌림
    -> 냄새는 상어가 k번 이동한 뒤 사라짐
    * 이동 방향 결정
        1. 인접한 칸 중 아무 냄새가 없는 칸의 방향
        2. 그런 칸이 없을 시, 자신의 냄새가 있는 칸의 방향으로
            - 가능한 칸이 여러 개일 시, 각 상어마다 주어진 우선순위를 따름
        3. 맨 처음의 방향은 입력으로 주어지고, 그 이후의 방향은 이동한 방향
        (보고있는 방향을 뜻함)
3. 모든 상어가 이동한 뒤, 한 칸에 여러 마리의 상어가 있다면
    -> 가장 작은 번호를 가진 상어를 제외하고 모두 쫓겨남

각 상어의 넘버에 따른 방향을 담을 1차원 배열
상어 냄새를 기록할 2차원 배열
상어 이동 우선순위가 담긴 2차원 배열 (입력)
상어 넘버를 담을 3차원 배열
** 상어 이동은 동시에 일어나고, 그 뒤에 그 칸에다가 동시에 냄새 뿌리는 거임
'''


def noob(i, j):
    return 0 <= i < N and 0 <= j < N


# 이 함수까지 완성시킨 다음에 유닛 테스트 ㄱ
def check_move(shark, i, j):
    '''
    * 이동 방향 결정
    1. 인접한 칸 중 아무 냄새가 없는 칸의 방향
    2. 그런 칸이 없을 시, 자신의 냄새가 있는 칸의 방향으로
        - 가능한 칸이 여러 개일 시, 각 상어마다 주어진 우선순위를 따름
    '''
    tmp = []
    for n in range(4):
        di, dj = DIR[n]
        ni, nj = i+di, j+dj
        if noob(ni, nj) and not scent[ni][nj]:
            tmp.append(n)

    # 다 돌았는데도 tmp가 비어있으면 인접한 칸 중에 아무 냄새가 없는 칸이 없다는 거
    # 그럼 내 냄새가 있는 방향으로 가주자
    if not tmp:
        for n in range(4):
            di, dj = DIR[n]
            ni, nj = i+di, j+dj
            if noob(ni, nj) and scent[ni][nj]:
                if scent[ni][nj][0] == shark:
                    tmp.append(n)
    return tmp


def move_shark():
    '''
    -> 그 칸에다가 자신의 냄새를 뿌림
    3. 맨 처음의 방향은 입력으로 주어지고, 그 이후의 방향은 이동한 방향
    '''
    remove_tmp = []  # 모아서 한 번에 지워줄 거예요
    shark_tmp = []  # 모아서 한 번에 이동시켜줄 거예요
    for i in range(N):
        for j in range(N):
            for k in range(len(sea[i][j])):
                if sea[i][j][k]:
                    shark = sea[i][j][k]
                    now_d = shark_info[shark]
                    c_lst = check_move(shark, i, j)  # 이동 가능한 칸 확인 / 가능한 이동 지점 lst로
                    if len(c_lst) > 1:  # 이동 가능한 지점이 2개 이상일 때
                        n = 0
                        m_lst = priority[shark][now_d]
                        will_d = m_lst[n]
                        while will_d not in c_lst:
                            n += 1
                            will_d = m_lst[n]
                    else:
                        will_d = c_lst[0]
                    shark_info[shark] = will_d  # 위치 바꿔줌
                    di, dj = DIR[will_d]  # 새로운 이동 방향 잡아줌
                    ni, nj = i + di, j + dj
                    remove_tmp.append([i, j])
                    shark_tmp.append([shark, ni, nj])

    for x, y in remove_tmp:
        sea[x][y] = []

    for shark, ni, nj in shark_tmp:
        sea[ni][nj].append(shark)

    return


def remove_scent():
    for i in range(N):
        for j in range(N):
            if scent[i][j]:
                scent[i][j][1] -= 1
                if scent[i][j][1] == 0:
                    scent[i][j] = []
    return


def make_scent():
    # -> 그 칸에다가 자신의 냄새를 뿌림 // 이동한 다음이니까 ni, nj칸에 뿌려주는 것
    for i in range(N):
        for j in range(N):
            for k in range(len(sea[i][j])):
                if sea[i][j][k]:
                    shark = sea[i][j][k]
                    scent[i][j] = [shark, K]
    return


# 상어 쫓아내기 운동 본부 1일차
def off_shark():
    '''
    3. 모든 상어가 이동한 뒤, 한 칸에 여러 마리의 상어가 있다면
    -> 가장 작은 번호를 가진 상어를 제외하고 모두 쫓겨남
    '''
    for i in range(N):
        for j in range(N):
            for k in range(len(sea[i][j])):
                if len(sea[i][j]) > 1:  # 두 마리 이상이 한 칸에 있을 때
                    sea[i][j].sort()  # 번호 작은 놈이 앞으로 오게
                    king_shark = sea[i][j][0] # 얘 빼고 다 내좇기
                    sea[i][j].pop(0)  # 일단 맨 앞에 애 빼주고
                    tmp = sea[i][j]  # tmp배열로 빼주기
                    for shark in tmp:
                        alive[shark] = False  # 죽여줘
                    sea[i][j] = []
                    sea[i][j].append(king_shark)

    return


N, M, K = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
# 위의 board를 sea로 옮겨줘야 함(3차원 배열)
sea = [[[] for _ in range(N)] for _ in range(N)]
shark_info = [[] for _ in range(M + 1)]
DIR = [(-1, 0), (1, 0), (0, -1), (0, 1)]
lst = list(map(lambda x:int(x)-1, input().split()))
for i in range(1, len(lst) + 1):
    shark_info[i] = lst[i-1]

priority = [[[] for _ in range(4)] for _ in range(M + 1)]
for i in range(1, M + 1):
    for j in range(4):
        priority[i][j] = list(map(lambda x:int(x)-1, input().split()))

scent = [[[] for _ in range(N)] for _ in range(N)]
alive = [True] * (M + 1)
alive[0] = False
# 맨 처음 각 상어가 자신의 위치에 자신의 냄새를 뿌림
for i in range(N):
    for j in range(N):
        if board[i][j] != 0:
            sea[i][j].append(board[i][j])  # 3차원 배열에 옮겨주고
            # scent[i][j] = [board[i][j], K]  # 그 상어의 냄새를 남겨줌
time = 0
while 1:
    make_scent()
    move_shark()
    remove_scent()  # 이동 횟수 기준으로 K가 감소함
    off_shark()
    # make_scent()
    time += 1

    a_flag = True
    for i in range(2, len(alive)):
        if alive[i]:
            a_flag = False
            break
    if a_flag:
        break
    if time > 1000 and not a_flag:
        break

if time > 1000:
    print(-1)
else:
    print(time)
