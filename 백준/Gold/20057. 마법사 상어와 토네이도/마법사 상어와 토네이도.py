import sys
input = sys.stdin.readline

def oob(i, j):
    return 0<=i<N and 0<=j<N

def move_sand(si, sj, dir, N):
    global cnt, total_sand
    # si, sj는 x에 해당하는 좌표값 dict에 각 방향에 맞는 이동 방향을 불러와서
    # ssi, ssj로 갱신해줄 것 // y에 해당하는 좌표
    while N > 0:
        # visited[si][sj] = 1
        now = 0
        percentage = dir_dict[dir]  # 현재 방향에 맞는 배열을 불러옴
        ti, tj = a_dict[dir]
        ssi, ssj = si+ti, sj+tj  # y위치

        if oob(ssi, ssj):
            now = tor[ssi][ssj]  # 현재 위치의 모래 양, 얘를 날려줄 거임
            tor[ssi][ssj] = 0

            tmp = 0
            for di, dj, perc in percentage:
                ni, nj = ssi+di, ssj+dj  # 모래가 흩날릴 위치셔요
                if oob(ni, nj):  # 만약 날리려는 위치가 범위 내에 있다면
                    ms = int(now * perc) # 이 녀석을 해당 위치에 넣어줄 거임
                    tor[ni][nj] += ms
                    tmp += ms
                elif not oob(ni, nj):
                    os = int(now*perc)
                    # total_sand += os
                    tmp += os

        # 이동한 모래들을 뺀 나머지를 a 자리에 넣어줄 거임
        now -= tmp
        # y위치에서 한 번 더 ti, tj 방향으로 이동한 a위치에 남은 거 넣어줌
        ai, aj = ssi+ti, ssj+tj
        if oob(ai, aj):
            tor[ai][aj] += now

        N -= 1
        si, sj = ssi, ssj  # 다음 턴을 위해 ... ;;
    cnt += 1
    return si, sj


N = int(input())
tor = [list(map(int, input().split())) for _ in range(N)]
visited = [[0]*N for _ in range(N)]
cnt = 0
# y기준 % 배열이 움직일 수 있는 방향 i, j, 해당하는 %
l_per = [(-2, 0, 0.02), (-1, 0, 0.07), (-1, 1, 0.01), (1, 1, 0.01), (2, 0, 0.02),
         (1, 0, 0.07), (1, -1, 0.1), (0, -2, 0.05), (-1, -1, 0.1)]
u_per = [(-2, 0, 0.05), (-1, 1, 0.1), (0, 2, 0.02), (0, 1, 0.07), (1, 1, 0.01),
         (1, -1, 0.01), (0, -2, 0.02), (0, -1, 0.07), (-1, -1, 0.1)]
d_per = [(-1, 1, 0.01), (0, 1, 0.07), (0, 2, 0.02), (1, 1, 0.1), (2, 0, 0.05),
         (1, -1, 0.1), (0, -2, 0.02), (0, -1, 0.07), (-1, -1, 0.01)]
r_per = [(-2, 0, 0.02), (-1, 0, 0.07), (-1, 1, 0.1), (0, 2, 0.05), (1, 1, 0.1),
         (2, 0, 0.02), (1, 0, 0.07), (1, -1, 0.01), (-1, -1, 0.01)]

dir_dict = {0:l_per, 1:d_per, 2:r_per, 3:u_per}
a_dict = {0:(0, -1), 1:(1, 0), 2:(0, 1), 3:(-1, 0)}

total_sand = 0
for lst in tor:
    total_sand += sum(lst)

si, sj = N//2, N//2
dir = 0
n = 1  # 처음에 길이 1만큼 움직이니까
num = N*2 - 1

total = 0
while num > 0:
    ci, cj = move_sand(si, sj, dir, n)

    si, sj = ci, cj

    if dir == 0: dir = 1
    elif dir == 1: dir = 2
    elif dir == 2: dir = 3
    else: dir = 0

    if cnt == 2:
        n += 1
        cnt = 0

    num -= 1

for lst in tor:
    total += sum(lst)
total_sand -= total

print(total_sand)