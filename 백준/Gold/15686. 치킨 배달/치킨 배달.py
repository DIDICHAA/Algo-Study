'''
1516
문제 이해)

구상)
전체의 치킨집 가운데, M개의 치킨집을 골라, 집부터 치킨집까지의 거리의 합을
min으로 갱신
치킨집이 위치한 곳을 전부 찾아서 튜플 형식으로 저장 -> 이걸 M개만큼 조합(백트래킹)
각각의 조합을 tmp lst에 담아서 함수 -> 해당 리스트 안에 담긴 좌표들 하나씩 꺼내면서
1까지의 거리를 계산하고 이를 min값에 저장 -> 이거 출력 (그냥 치킨 거리 최솟값이니까)

1528 : 구현 시작
1547 : 디버깅 시작


대박 바보짓 1.
치킨집과 집과의 거리를 bfs로 구하려고 했는데
... 그냥 r, c 좌표값끼리 빼준 값을 갱신해주면 되잖아?
이걸로
무려
1시간을 보냄 하하하
다른 문제에서부터 안 틀리면 되니까 ㄱㅊ

2. 조합 이슈
걍 조합이 안 돌아가심;
0 1 2 다음에 0 1 3이 와야 되는데 지금 코드로는 3 4 5가 오려고 함
말이 되니 백트래킹 다시 공부하길...

50*50 = 2500
'''

def cal_mins(lst):  # 2에서 1까지의 거리를 갱신하는 함수
    global real_total
    total = 0

    for hi, hj in house:
        ans = 1e9
        tmp = 0
        for ci, cj in lst:
            tmp = (abs(ci-hi) + abs(cj-hj))
            ans = min(tmp, ans)
        total += ans
    real_total = min(real_total, total)


def make_combs(n, idx):

    if n == M:
        cal_mins(comb_lst)
        return

    for k in range(idx, len(chicken)):
        comb_lst.append(chicken[k])
        make_combs(n+1, k+1)
        comb_lst.pop()


N, M = map(int, input().split())
village = [list(map(int, input().split())) for _ in range(N)]

chicken = []  # 치킨집 위치를 담을 리스트
house = []  # 집 위치를 담을 리스트
comb_lst = []
real_total = 1e9

dir = [(0, 1), (0, -1), (1, 0), (-1, 0)]
visited = [[0]*N for _ in range(N)]

for i in range(N):
    for j in range(N):
        if village[i][j] == 2:
            chicken.append((i, j)) # 치킨집의 위치를 튜플로 저장

        if village[i][j] == 1:
            house.append((i, j))  # 집의 위치를 튜플로 저장

make_combs(0, 0)  # M개만큼의 치킨집을 찾을 조합

print(real_total)