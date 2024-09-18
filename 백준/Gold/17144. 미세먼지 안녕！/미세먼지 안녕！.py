'''
미세먼지 안녕!
[ 마음 가짐 ]
** 2시간 잡고 풀어보기 **
** 구현 문제일수록 꼼꼼하게 읽고 요구하는 대로 구현하기**
** 뇌피셜로 해석하기 금지 **


2150 문제 이해)

공기 청정기는 항상 1번 열에 설치, 크기는 두 행을 차지

< 1초 동안 일어나는 일 >

1. 미세먼지 확산, 모든 칸에서 동시에 일어남 (bfs의 느낌 강렬하게 나기 시작)
    -> 인접한 네 방향으로 확산, 인접한 방향에 공청기가 있거나 oob면 확산이 일어나지 않음
    -> 확산되는 양은 해당 칸의 //5
    -> 남은 미세먼지의 양은 해당 칸 - 확산량 * 확산된 방향의 개수

2. 공기청정기 작동
    -> 위쪽 공청기 바람은 반시계 방향으로 순환
    -> 아레쪽 공청기 바람은 시계 방향으로 순환
    -> 바람이 불면 미세먼지가 바람의 방향대로 모두 한 칸씩 이동
    -> 공청기에서 부는 바람은 미세먼지가 없는 바람
    ** -> 공청기로 들어간 미세먼지는 모두 정화!

** 공청기가 두 칸을 차지한다고 했잖아 거기서 위칸은 열대로 쭉 갔다가 위로 가서 왼쪽으로 가는 반시계 방향 순환이고
   아래 칸은 열로 쭉 갔다가 아래로 간 다음에 왼쪽으로 가는 시계 방향 순환임

출력 : T초가 지난 뒤, 구사과씨의 방에 남은 미세먼지 양을 구하라 !!

2156 구상)
[ 공청기 작동 함수 ]
[ 미세먼지 확산 함수 ]
[ main ]
주어진 조건 대로만 잘 구현하자 !! oob 체크랑 칸 이동 잘 확인하기

2159 구현)

'''
from collections import deque

def oob(i, j):
    return 0<=i<R and 0<=j<C

def turn_air():
    global room

    q = deque()
    for i in range(R):
        for j in range(C):
            # 공청기도, 0도 아닐 때 // 미세먼지가 있는 칸일 떄
            if room[i][j] != -1 and room[i][j] != 0:
                q.append((i, j))

    # tmp_room = [lst[:] for lst in room]
    tmp_room = [[0]*C for _ in range(R)]
    tmp_room[topi][topj] = -1
    tmp_room[boti][botj] = -1

    while q:
        ci, cj = q.popleft()
        cnt = 0
        for di, dj in dir:
            ni, nj = ci+di, cj+dj
            if oob(ni, nj) and room[ni][nj] != -1:
                num = room[ci][cj] // 5  # 확산시킬 미세먼지의 양
                tmp_room[ni][nj] += num  # 확산 완.
                cnt += 1
        # 어차피 0이면 계산해봤자 값 똑같으니까 1군데 이상 퍼졌을 때 미세먼지 원래 위칫값은 저렇게 갱신
        if cnt > 0:
            tmp = room[ci][cj] - (room[ci][cj]//5 * cnt)
            tmp_room[ci][cj] += tmp

    room = tmp_room
    return


def extend_mise_up():
    global room
    # 위쪽 부분만한 배열을 만들어볼까 .. 만들고 비교해서 넣고 덮어 씌워볼까...
    tmp_top = [[0]*C for _ in range(R)]
    tmp_top[topi][topj] = -1  # 그래도 공청기 위치는 표시해줘야 안 헷갈려잉

    # 맨 아랫 열 오른쪽 쭉
    for j in range(C-1):
        if room[topi][j] != -1:
            tmp_top[topi][j+1] = room[topi][j]

    # 맨 오른쪽 열 위로 쭉
    for i in range(topi-1, -1, -1):
        if room[i+1][C-1] != -1:
            tmp_top[i][C-1] = room[i+1][C-1]

    # 맨 위쪽 열 왼쪽으로 쭉
    for j in range(C-1, 0, -1):
        if room[0][j] != -1:
            tmp_top[0][j-1] = room[0][j]

    # 맨 왼쪽 열 아래쪽으로 쭉
    for i in range(topi-1):
        if room[i][0] != -1:
            tmp_top[i+1][0] = room[i][0]

    for i in range(1, topi):
        for j in range(topj+1, C-1):
            tmp_top[i][j] = room[i][j]

    for i in range(topi+1):
        for j in range(topj, C):
            room[i][j] = tmp_top[i][j]

    return


def extend_mise_down():
    global room
    tmp_down = [[0]*C for _ in range(R)]
    tmp_down[boti][botj] = -1  # 그래도 공청기 위치는 표시해줘야 안 헷갈려잉

    # 맨 윗 열 오른쪽 쭉
    for j in range(C-1):
        if room[boti][j] != -1:
            tmp_down[boti][j+1] = room[boti][j]

    # 맨 오른쪽 열 아래로 쭉
    for i in range(boti, R-1):
        if room[i+1][C-1] != -1:
            tmp_down[i+1][C-1] = room[i][C-1]

    # 맨 아래쪽 열 왼쪽으로 쭉
    for j in range(C-1, 0, -1):
        if room[R-1][j] != -1:
            tmp_down[R-1][j-1] = room[R-1][j]

    # 맨 왼쪽 열 위로 쭉
    for i in range(R-1, boti-1, -1):
        if room[i-1][0] != -1:
            tmp_down[i-1][0] = room[i][0]

    # 중간값 채우기
    for i in range(boti+1, R-1):
        for j in range(botj+1, C-1):
            tmp_down[i][j] = room[i][j]

    for i in range(boti, R):
        for j in range(botj, C):
            room[i][j] = tmp_down[i][j]
    return


R, C, T = map(int, input().split())
room = [list(map(int, input().split())) for _ in range(R)]
dir = [(0, 1), (0, -1), (1, 0), (-1, 0)]

air_puri = []
for i in range(R):
    for j in range(C):
        if room[i][j] == -1:
            air_puri.append((i, j))

# 공청기의 윗 부분과 아랫 부분 인덱스를 잡아주기
topi, topj= air_puri[0]
boti, botj = air_puri[-1]

while T > 0:
    turn_air()
    extend_mise_up()
    extend_mise_down()
    T -= 1

total = 0
for i in range(R):
    for j in range(C):
        if room[i][j] != -1:
            total += room[i][j]

print(total)