'''
** 배열 여러 개로 나눠서 관리하기 **
** 함수 별로 테스트 정확하게 하고 넘어가기 **
** 조급하게 풀지 말기!!!!!!! **
** 라인 별로 의미 생각하면서 풀기 **

문제 이해
* 좌표값 -1씩 해주기
격자에는 물고기 M마리, 각 격자에는 물고기 한 마리씩 w 이동 방향 (8방)
둘 이상의 물고기가 같은 칸에 있을 수도 있고, 상어랑 물고기가 같은 칸에 있을 수도 있다

1. 모든 물고기에게 복제 마법 - 5번에서 시현됨
2. 모든 물고기 한 칸 이동
    - 상어가 있는 칸, 물고기 냄새가 있는 칸, oob는 이동 불가능
    - 각 물고기는 자신이 가지고 있는 이동 방향이 이동할 수 있는 칸을 향할 때까지 반시계 45도 회전
        - > 이동할 수 있는 칸이 없다면 이동하지 않음 / 그 외에는 이동
3. 상어가 연속해서 3칸 이동
    - 현재 칸에서 4방으로 이동 가능
    - 이동 가능 칸 중 oob가 있으면 그 방법은 불가능한 이동 방법
    - 연속해서 이동하는 중, 물고기가 있는 칸으로 이동 시
        -> 그 칸에 있는 모든 물고기 격자에서 사라짐
        -> 물고기 냄새를 남김
    - 가능한 이동 방법 중, 제외되는 물고기 수가 가장 많은 방법으로 이동
        -> 여러가지라면 사전 순으로 앞서는 방법
4. 두 턴 전에서 생긴 물고기의 냄새가 사라짐 (물고기의 냄새는 2로 넣어줘야 겠네요)
5. 1번에서 사용한 복제 마법 시전 - 복제된 물고기는 1에서의 위치와 방향을 그대로 가짐

출력 : S번의 연습을 마쳤을 때, 격자에 남아있는 물고기의 수는?

사전 :
1:상, 2:좌, 3:하, 4:우
그니까 이어서 만든 세 개의 방향에 해당하는 숫자가 더 작을 수록 더 우선하는 거
상상상 > 상좌하
111 123 이니까 숫자가 더 적은 111이 사전적으로 우선

구상)
각 넘버마다 모듈로 짜면 될 듯 ...
위 마음가짐 명심하면서 ... !!!
'''
from collections import deque
def noob(i, j):
    return 0<=i<4 and 0<=j<4

def move_fish():
    global fish

    fish_tmp = [[[] for _ in range(4)] for _ in range(4)]
    for i in range(4):
        for j in range(4):
            for k in range(len(fish[i][j])):
                if fish[i][j][k] is not None:
                    d = fish[i][j][k]
                    cnt = 0

                    di, dj = DIR_fish[d]
                    ni, nj = i + di, j + dj

                    if noob(ni, nj) and (ni, nj) != (sx, sy) and scent[ni][nj] == 0:
                        fish_tmp[ni][nj].append(d)

                    else:
                        while 1:
                            if cnt == 8:
                                fish_tmp[i][j].append(fish[i][j][k])
                                break
                            if noob(ni, nj) and (ni, nj) != (sx, sy) and scent[ni][nj] == 0:
                                fish_tmp[ni][nj].append(d)
                                break
                            d = (d-1) % 8
                            cnt += 1
                            di, dj = DIR_fish[d]
                            ni, nj = i + di, j + dj

    fish = fish_tmp
    return

def move_shark():
    # 연속해서 이동하는 3칸 모두 noob여야 함
    # 완탐 하자!
    global sx, sy

    whole_tmp = []
    for n in range(len(DIR_shark)):
        si, sj = sx, sy
        total, cnt = 0, 0
        tmp = []
        visited = [[False]*4 for _ in range(4)]

        for di, dj in DIR_shark[n]:
            ni, nj = si+di, sj+dj
            if not noob(ni, nj):
                break
            if fish[ni][nj] and not visited[ni][nj]:
                visited[ni][nj] = True
                total += len(fish[ni][nj])
            tmp.append((ni, nj))
            cnt += 1
            si, sj = ni, nj
            if cnt == 3:
                whole_tmp.append((-total, n, tmp))

    whole_tmp.sort()
    _, _, lst = whole_tmp[0]

    for n in range(len(lst)):
        ci, cj = lst[n]
        if fish[ci][cj]:
            scent[ci][cj] = 2
        fish[ci][cj] = []  # 상어한테 잡아 먹힘

    sx, sy = lst[-1]
    return


def remove_scent():
    for i in range(4):
        for j in range(4):
            if scent[i][j] > 0:
                scent[i][j] -= 1
    return


def copy_fish(arr):
    global fish

    for i in range(4):
        for j in range(4):
            for k in range(len(arr[i][j])):
                fish[i][j].append(arr[i][j][k])
    return


M, S = map(int, input().split())
fish = [[[] for _ in range(4)] for _ in range(4)]  # 물고기만 담을 거야
scent = [[0 for _ in range(4)] for _ in range(4)]  # 냄새만 담을 거야
DIR = [(-1, 0), (0, -1), (1, 0), (0, 1)]
DIR_fish = [(0, -1), (-1, -1), (-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1)]

# 가능한 상어 이동 조합을 만들고 시작
DIR_shark = []
for i in range(4):
    for j in range(4):
        for k in range(4):
            x, y, z = DIR[i], DIR[j], DIR[k]
            DIR_shark.append((x, y, z))

for _ in range(M):
    fx, fy, d = map(int, input().split())
    fish[fx-1][fy-1].append(d-1)

sx, sy = map(int, input().split())
sx -= 1
sy -= 1

for t in range(S):
    tmp_fish = [lst[:] for lst in fish]
    move_fish()
    if t > 0:
        remove_scent()
    move_shark()
    copy_fish(tmp_fish)

ans = 0
for i in range(4):
    for j in range(4):
        ans += len(fish[i][j])
print(ans)