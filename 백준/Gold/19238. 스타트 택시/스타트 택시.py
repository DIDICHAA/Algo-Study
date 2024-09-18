'''
1000 문제 이해
백준은 특정 위치로 이동할 때 항상 최단 경로로만 이동
M명의 승객 - 빈칸 중 하나 -> 다른 빈칸 중 하나로 이동 // 승객은 1명씩 탑승
출발지에서만 타고, 목적지에서만 내림
1. 현재 위치에서 최단 거리가 가장 짧은 승객
    -> 여러 명이라면 그 중 행 번호가 가장 작은 승객
        -> 여러 명이라면 열 번호가 가장 작은 승객
    // 택시와 승객이 같은 위치 : 최단 거리 0

2. 연료는 한 칸 이동 시마다 1씩 소모
3. 한 승객을 목적지로 성공적으로 이동 - 그 승객을 태워 이동하며 소모한 연료 양 2배 충전
    -> 태우러 가기까지의 연료는 포함되지 않음
4. 이동하는 도중 연료가 0이 되면 실패, 업무 끝
    -> 목적지에 도착함과 동시에 연료가 0이 된 건 성공

모든 손님 이동 + 연료 충전 : 남은 연료 양 출력
이동 도중 연료 바닥 or 모든 손님 이동 불가 : - 1 출력

~1010
구상)
bfs 써서 최단 거리 알아내고, // bfs 들어갈 때마다 배열 새로 선언
전체 돌면서 v 처리 -> 각 승객이 서있는 좌표의 값(최단 거리) 기준으로 소팅(최단거리, num, i, j)
그리고 전체 연료에서 최단 거리만큼 일단 빼주고,
승객이 있는 점까지 갔으면 목적지까지 for문으로 거리 계산 해줌
    -> if 연료 충분 - 킵고잉
    -> 아니면 함수 빠져나오고 return -1

1010~ 구현

1118~ 디버깅
1. 런타임 에러
~ 시도한 해결 방법 ~
    -> return 값을 안 써줘서 추가 함
        -> 그냥 런타임 에러에서 1% 런타임 에러로 바뀜;
    ->
'''
from collections import deque

def oob(i, j):
    return 0<=i<N and 0<=j<N

# 승객을 찾는 bfs
def find_shortest(si, sj):
    q = deque()
    visited = [[0]*N for _ in range(N)]
    visited[si][sj] = 1
    q.append((si, sj))

    while q:
        ci, cj = q.popleft()
        for di, dj in dir:
            ni, nj = ci+di, cj+dj
            if oob(ni, nj) and visited[ni][nj] == 0 and jido[ni][nj] != 1:
                visited[ni][nj] = visited[ci][cj] + 1
                q.append((ni, nj))

    tmp = []
    for i in range(N):
        for j in range(N):
            for k in range(len(customers[i][j])):
                if customers[i][j][k] in customer_list:
                    length = visited[i][j] - 1
                    tmp.append([length, i, j, customers[i][j][k]])

    tmp.sort()
    now_customer = tmp[0]
    distance, i, j, start = now_customer
    # 현 시점에서 먼저 데려다 줄 승객 return
    return distance, i, j, start


def find_destination(si, sj, K):
    q = deque()
    visited = [[0]*N for _ in range(N)]
    visited[si][sj] = 1
    q.append((si, sj))

    while q:
        ci, cj = q.popleft()
        for di, dj in dir:
            ni, nj = ci+di, cj+dj
            if oob(ni, nj):
                if visited[ni][nj] == 0 and jido[ni][nj] != 1:
                    visited[ni][nj] = visited[ci][cj] + 1
                    q.append((ni, nj))


    destination_dis = 0
    for i in range(N):
        for j in range(N):
            if -K in customers[i][j]:
                if visited[i][j] != 0: # 데려다 줄 수 있을 때
                    destination_dis = visited[i][j] - 1
                    return destination_dis, i, j
                else:
                    destination_dis = -1
                    return destination_dis, i, j
    return


N, M, fuel = map(int, input().split())
jido = [list(map(int, input().split())) for _ in range(N)]
si, sj = map(int, input().split())
si -= 1
sj -= 1

customers = [[[] for _ in range(N)] for _ in range(N)]
# 지도 상에 승객 별 탑승지/목적지 마킹 - bfs에서 사용
for k in range(2, M+2):
    i, j, ei, ej = map(int, input().split())
    customers[i-1][j-1].append(k)
    customers[ei-1][ej-1].append(-k)

    # 탑승 위치랑 하차 위치가 여러 개 겹칠 때 ... 값이 덮어 씌워지니까 오류가 남


customer_list = [i for i in range(2, M+2)]
dir = [(0, 1), (0, -1), (1, 0), (-1, 0)]
num = len(customer_list)
flag = True

while num > 0:
    # 현재 위치에서 탑승 거리가 가장 작은 승객
    distance, cus_i, cus_j, start = find_shortest(si, sj)
    if distance == -1:
        flag = False
        break

    fuel -= distance  # 승객 태우러 간 거리만큼 빼줌

    if fuel < 0:
        flag = False
        break

    destination_dis, ddi, ddj = find_destination(cus_i, cus_j, start)
    if destination_dis == -1:
        flag = False
        break

    fuel -= destination_dis

    if fuel < 0:
        flag = False
        break

    fuel += (destination_dis)*2  # 두 배가 돼 두 두배 두배두

    cus_tmp = []
    for i in range(len(customer_list)):
        if customer_list[i] != start:
            cus_tmp.append(customer_list[i])
    customer_list = cus_tmp

    si, sj = ddi, ddj
    num -= 1

if customer_list:
    flag = False

if flag:
    print(fuel)
else:
    print(-1)