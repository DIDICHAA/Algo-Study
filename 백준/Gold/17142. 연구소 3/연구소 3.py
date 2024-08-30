'''
연구소 3!
[ bfs 방문처리 조건 실수 금지; ]

0907 문제 이해)
visited[ni][nj] = visited[ci][cj] + 1로 표시
최소 시간을 구하라고 했으니 bfs로 탐색하는 것이 좋을 듯 함

구상)
1. 비활성 바이러스 기준 (while, visited는 전역) 탐색
2. bfs 방문처리 기준 // 벽일 때는 갈 수 없음
바이러스가 더 가까울 경우 그 지점에서부터 퍼트려나가면 될 듯

0914 구현)
앗 문제 이해에서 실수 발견
M개의 바이러스 만을 활성화 시키는 거 바이러스는 그냥 0으로 표시
백트래킹(조합) + 그래프 탐색;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
아니 어렵잖아!!!!!!!!!!!!!!!!!!
문제 관상 : 골드 2~3으로 추측 / 겉보기엔 4정도인 척 하는 게 특징

0946 디버깅)
< 애매하게 구현했다고 생각하는 부분>
1. collect_virus에서 내가 생각한대로 0 좌표 조합이 잘 짜졌는지
2. bfs에서 내가 생각한대로 바이러스가 잘 퍼졌는지
3. check_time에서 min값은 잘 갱신되었는지

<디버깅 리스트>ㅋㅋ;
1. 나의 코드가 영원히 끝나지 않아버림
-> 이유 !! 조합 돌릴 떄 lst를 비워주고, 1 2 3 을 골랐으면 다음 번에는 1 2 4를 고를 수 있게 해줘야 하는데,
지금 내 코드는 1 2 3 4 5 6 4 5 6 5 6.. 이런 식으로 영원히 끝나지 않을 조합을 만들어버림;;

일단 조합 이슈는 해결
min값이 제대로 갱신이 안 되는 이슈 // 아마도 bfs안에서 si, sj가 동시다발적으로 안 일어나고 있기 때문이 아닐까 하는 추측
-> 왜냐면 min값이 21이 나옴; // bfs 시작점을 1로 해서 1만큼 더 나오는 이슈 해결

마지막 이슈!!!!
-1이 나올 떄와 0일 때 !! main에서 if문 분기하고, -1은 print 안 찍어줘서 그런 거라 해결

1100
.. 69퍼센트 틀렸습니다 이슈
크기가 큰 테케가 문제가 아니라, 내가 고려 못한 사이드 테케가 있는 듯 T.T

시도1. flag 위치가 else 아래로 들어가야 해서 (요건 맞음) 그래서 옮겨줌 - 여전히 69퍼 실패
시도2. N*M으로 초기화시켰던 mini의 값을 N*N으로 해줌 - ㅎ; 81퍼 실패 미쳤나
시도3. 엣지 케이스를 찾아라!!!!!!!!!!!!!!!!!!!

'''

from collections import deque


# oob 관련 처리
def oob(i, j):
    return 0 <= i < N and 0 <= j < N

def check_time(visited):
    global mini, flag

    for i in range(N):
        for j in range(N):
            # 하나라도 못들어간 녀석이 있다면 얘는 못 쓰는 녀석임
            if lab[i][j] == 0 and visited[i][j] == 0:
                return

    # lab 상에서 0이었고, visited 처리가 돼 있는 값 중에서의 max 값
    # 그리고 전체 중에 이 max 값이 가장 작은 녀석을 mini로 넣어줘야 함
            if lab[i][j] == 2 and visited[i][j] != 1:
                visited[i][j] = 0

    tv = sum(visited, [])
    num = max(tv) - 1
    mini = min(mini, num)
    flag = True  # 한 번이라도 바이러스가 완전히 퍼졌다면



# M개의 시작 좌표를 만들고 bfs로 쏴주는 함수
def collect_virus(n, s, lst):

    if n == M:
        visited = [[0] * N for _ in range(N)]
        bfs(lst, visited)
        check_time(visited)
        return

    for i in range(s, len(tmp)):
        lst.append(tmp[i])
        collect_virus(n+1, i+1, lst)
        lst.pop()


# 바이러스를 전파시키는 bfs
def bfs(lst, visited):
    q = deque()

    # M개의 조합으로 만들어진 바이러스 시작 위치를 모두 q에 넣어줌 / si, sj로 잡아준다는 뜻
    for i, j in lst:
        si, sj = i, j
        visited[si][sj] = 1
        q.append((si, sj))

    # tmp에 있고 lst에 안 담긴 2의 좌표들이라 때는 +1을 안 해주고, 건너뛴 다음부터 +1을 해줌 continue의 느낌
    while q:
        ci, cj = q.popleft()
        for di, dj in dir:
            ni, nj = ci+di, cj+dj

            if oob(ni, nj) and visited[ni][nj] == 0 and lab[ni][nj] != 1:
                visited[ni][nj] = visited[ci][cj] + 1
                q.append((ni, nj))


N, M = map(int, input().split())
lab = [list(map(int, input().split())) for _ in range(N)]
dir = [(0, 1), (0, -1), (1, 0), (-1, 0)]
mini = N*N  # 최대로 나올 수 있는 min값이 배열의 사이즈 - 1임 (달팽이 모양처럼 돼 있을 때)
flag = False

# 바이러스가 있는 모든 좌표를 tmp에 넣어줌
tmp = []
for i in range(N):
    for j in range(N):
        if lab[i][j] == 2:
            tmp.append((i, j))

tl = sum(lab, [])
if tl.count(0) == 0:  # 빈 방이 하나도 없을 때
    print(0)
else:
    collect_virus(0, 0, [])  # 바이러스가 M개가 되는 좌표의 조합을 구하는 함수
    if not flag:
        print(-1)
    else:
        print(mini)