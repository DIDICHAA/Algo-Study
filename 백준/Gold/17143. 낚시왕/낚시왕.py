'''
0900 문제 이해)
0,0에서 시작, N-1, N-1에 도달하면 멈춤

1. 낚시왕이 오른쪽으로 한 칸 이동(0, 1)
2. 낚시왕이 위치한 열 중, 땅과 가장 가까운 상어를 포획 / 상어는 격자에서 사라짐
3. 상어 이동
    -> 입력으로 주어진 속도로 이동, 속도의 단위는 칸/초
    -> oob가 될 시 방향을 반대로 바꿔서 속력 유지한 채 이동
    -> 상어 이동 후, 한 칸에 상어가 2마리 이상 있다면 크기가 가장 큰 상어만 남음

출력 : 낚시왕이 잡은 상어 크기의 합

구상) 적은 순서대로 구현하되, 1초에 몇 칸을 가는 지를 받아서 mul값으로 곱해서 ni, nj 설정
3차원 배열로 접근해서 사용해야 될 듯 / 상어 정보 들고 움직이려면
각 열마다 있는 지 확인하는 건 check_shark 배열에서 j값 i에다 넣고 보면 됨

0904
구현 시작!
!! 애초에 두 마리 이상이 존재할 수 없음 저 get_shark 함수에서는
왜냐면 내가 move_shark 함수에서 다 죽일 거기 때문에
..
다버깅 리스트
1. 상어들은 모아놨다가 한 번에 움직여 줘야 한다. .. 안 그러면 여러 번 움직이는 상어가 발생하니께

'''


def oob(i, j):
    return 0<=i<R and 0<=j<C


def check_direction(s, d, i, j):
    cnt = 0

    if d == 1:
        s %= standard_r
        while s > 0:
            while i > 0 and s > 0:
                i -= 1
                s -= 1
            if i == 0:
                cnt += 1
                while i < R-1 and s > 0:
                    i += 1
                    s -= 1
                if i == R-1:
                    cnt += 1

    elif d == 2:
        s %= standard_r
        while 0 <= i < R and s > 0:
            while i != R - 1 and s > 0:
                i += 1
                s -= 1
            if i == R-1:
                cnt += 1
            while i != 0 and s > 0:
                i -= 1
                s -= 1
            if i == 0:
                cnt += 1

    elif d == 3:
        s %= standard_c
        while 0 <= j < C and s > 0:
            while j != C - 1 and s > 0:
                j += 1
                s -= 1
            if j == C-1:
                cnt += 1
            while j != 0 and s > 0:
                j -= 1
                s -= 1
            if j == 0:
                cnt += 1

    else:
        s %= standard_c
        while s > 0:
            while j > 0 and s > 0:
                j -= 1
                s -= 1
            if j == 0:
                cnt += 1
                while j < C-1 and s > 0:
                    j += 1
                    s -= 1
                if j == C-1:
                    cnt += 1

    if cnt % 2 == 1:
        if d == 1 or d == 3:
            d += 1
        else:
            d -= 1

    return d


def switch_shark(i, j, ni, nj, S):
    cnt = 0
    if ni >= R:
        while 0 <= i < R and S > 0:
            while i != R - 1 and S > 0:
                i += 1
                S -= 1
            while i != 0 and S > 0:
                i -= 1
                S -= 1

    if nj >= C:
        while 0 <= j < C and S > 0:
            while j != C-1 and S > 0:
                j += 1
                S -= 1
            while j != 0 and S > 0:
                j -= 1
                S -= 1

    if ni < 0:
        S = S % standard_r
        while S > 0:
            while i > 0 and S > 0:
                i -= 1
                S -= 1
            if i == 0:
                while i < R-1 and S > 0:
                    i += 1
                    S -= 1

    if nj < 0:
        S = S % standard_c
        while S > 0:
            while j > 0 and S > 0:
                j -= 1
                S -= 1
            if j == 0:
                while j < C-1 and S > 0:
                    j += 1
                    S -= 1

    return i, j


# 상어가 이동하는 로직
def move_shark():
    # 3차원 배열 속 s, d값에 따라 이동시켜주고 return
    # 하... 모아 놨다가 한 번에 처리해줘야 함
    will_move = []
    for i in range(R):
        for j in range(C):
            for k in range(len(sharks[i][j])):
                z, s, d = sharks[i][j][k]
                di, dj = dir[d]
                ni, nj = i+di*s, j+dj*s
                # 범위 안 벗어나면 그 방향 그대로
                if oob(ni, nj):
                    a, b, c = sharks[i][j][k]
                    tmp2 = []
                    for x, y, zz in sharks[i][j]:
                        if a != x and b != y and c != zz:
                            tmp2.append([x, y, zz])
                    sharks[i][j] = tmp2  # 기존 위치에서는 없애주고
                    will_move.append([ni, nj, z, s, d])  # 이동한 위치에 정보 추가
                else:
                    d = check_direction(s, d, i, j)

                    # 얘네를 묶어서 oob 검증 -> 아니면 바꿔서 나오는 함수를 빼자
                    if not oob(ni, nj):
                        ni, nj = switch_shark(i, j, ni, nj, s)

                    # 여기서 방향이 바뀌었을 수 있으니 ni, nj값을 다시 잡아줘야 함
                    a, b, c = sharks[i][j][k]
                    tmp2 = []
                    for x, y, zz in sharks[i][j]:
                        if a!=x and b!=y and c!=zz:
                            tmp2.append([x, y, zz])
                    sharks[i][j] = tmp2
                    will_move.append([ni, nj, z, s, d])

    # print(*will_move)
    for ni, nj, z, s, d in will_move:
        sharks[ni][nj].append([z, s, d])

    # 한 칸에 상어가 두 마리 이상 있을 시, 가장 큰 놈만 살아남는 로직
    # 근데 지금 작은 놈이 살아있는 듯 ㄷㄷ
    ttmp = []
    for i in range(R):
        for j in range(C):
            length = len(sharks[i][j])
            if length >= 2:
                sharks[i][j].sort(reverse=True)
                a, b, c = sharks[i][j][0]
                ttmp.append([i, j, a, b, c])

    for i, j, a, b, c in ttmp:
        sharks[i][j] = []
        sharks[i][j].append([a, b, c])
    return


def get_shark(si, sj):
    global total

    num = C
    now = sj
    while num > 0:
        # 현재 낚시왕이 서있는 열에서 가장 가까운 상어를 잡음
        for i in range(R):
            if sharks[i][now]:
                z, s, d = sharks[i][now][0]
                total += z  # 가장 가까운 상어를 잡음
                tmp = []
                sharks[i][now] = tmp
                break

        # print(*sharks, sep='\n')
        # print('################')
        move_shark()
        num -= 1
        now += 1
    return


R, C, M = map(int, input().split())
sharks = [[[] for _ in range(C)] for _ in range(R)]
standard_r = 2 * (R - 1)
standard_c = 2 * (C - 1)

for _ in range(M):
    r, c, s, d, z = map(int, input().split())
    sharks[r-1][c-1].append([z, s, d])

total = 0  # 잡은 상어의 크기를 뽑아낼 것
dir = {1:(-1, 0), 2:(1, 0), 3:(0, 1), 4:(0, -1)}  # 상 하 우 좌
get_shark(0, 0)
print(total)