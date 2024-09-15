'''
1635 문제 이해)
학생 번호는 1 ~ N^2
교실은 (1,1) 에서 (N, N)까지 있음
한 칸에는 한 명만 앉을 수 있고, 4방만 인접한 칸

1. 비어있는 칸 중 좋아하는 학생이 인접한 칸에 가장 많은 칸에 자리를 정함
2. 1번을 만족하는 칸이 여러 개라면, 인접한 칸 중 비어있는 칸이 가장 많은 칸으로 자리를 정함
3. 2번을 만족하는 칸도 여러 개인 경우, 행 - 열 순으로 번호가 가장 작은 칸으로 자리를 정함

ㅎ. 위 조건을 만족시키면서 학생들을 계속 앉혀야 함
전부 다 조건에 맞게 앉힌 다음, 학생 만족도의 총합을 출력하면 됨

1639 구상 및 구현)
주어진 조건 그대로 구현하되, 주어진 예제와 동일하게 앉혔나 유닛 테스트 하면서 진행하기

1757 디버깅
이슈 1. 테케 넣었더니 얘네가 자리에 도통 앉질 않고 다 도망감; 이거 해결하면 될 듯
'''
def oob(i, j):
    return 0<=i<N and 0<=j<N


def sit_students(me, l1, l2, l3, l4):
    like_lst = [l1, l2, l3, l4]

    maxi = 0
    tmp = []
    # 1번 조건 먼저 따져보기
    for i in range(N):
        for j in range(N):
            cnt = 0
            if shark_class[i][j] != 0: continue
            for di, dj in dir:
                ni, nj = i+di, j+dj
                if oob(ni, nj) and shark_class[ni][nj] in like_lst:
                    cnt += 1
            maxi = max(maxi, cnt)
            tmp.append((cnt, -(i+1), -(j+1)))

    tmp_2 = []

    # 여기서 지금 냅다 소팅 해버려서 cnt가 맨 위로 오긴 하는데 i, j 정렬이 생각한 대로 나오지는 않음

    tmp.sort(reverse=True)
    for cnt_1, i1, j1 in tmp:
        if cnt_1 == maxi:
            tmp_2.append((cnt_1, i1, j1))

    t_maxi = 0
    # 1번 조건에 해당하는 자리가 여러 개일 경우
    tmp_3 = []
    for _, x, y in tmp_2:
        x = -x - 1
        y = -y - 1
        t_cnt = 0
        for dx, dy in dir:
            nx, ny = x+dx, y+dy
            if oob(nx, ny) and shark_class[nx][ny] == 0:
                t_cnt += 1
        t_maxi = max(t_maxi, t_cnt)
        tmp_3.append((t_cnt, -(x+1), -(y+1)))

    # 2번 조건을 만족하는 자리도 여러 개일 경우
    tmp_4 = []
    for cnt_2, i2, j2 in tmp_3:
        i2 = -i2 - 1
        j2 = -j2 - 1
        if t_maxi == cnt_2:
            tmp_4.append((cnt_2, i2, j2))

    _, fi, fj = tmp_4[0]

    shark_class[fi][fj] = me
    return


N = int(input())
students = [list(map(int, input().split())) for _ in range(N**2)]
shark_class = [[0]*N for _ in range(N)]
dir = [(0, 1), (0, -1), (1, 0), (-1, 0)]
score = {0:0, 1:1, 2:10, 3:100, 4:1000}

for lst in students:
    me, l1, l2, l3, l4 = lst
    sit_students(me, l1, l2, l3, l4)

total = 0
# 전부 다 앉힌 뒤, 만족도 조사하기
for lst in students:
    me, l1, l2, l3, l4 = lst
    for i in range(N):
        for j in range(N):
            cnt = 0
            if shark_class[i][j] == me:
                for di, dj in dir:
                    ni, nj = i+di, j+dj
                    if oob(ni, nj) and (shark_class[ni][nj] == l1 or shark_class[ni][nj] == l2 or shark_class[ni][nj] == l3 or shark_class[ni][nj] == l4):
                        cnt += 1
                total += score[cnt]
print(total)