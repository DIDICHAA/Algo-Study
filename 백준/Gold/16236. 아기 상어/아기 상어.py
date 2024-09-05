'''

1. 먹을 수 있는 물고기가 한 마리 이상 남아있다면
    -> 얘 먹으러 가고, i / j 정렬 순으로 찾아감
        -> 먹을 수 있는 물고기의 기준(lst)은 현재 아기 상어보다 작아야 하고,
        -> visited 거리 상에서 가장 가까운 순이어야 함
            => visited를 먼저 다 채운 뒤, sea[ci][cj]의 값이 baby 보다 작고, visited[ci][cj]값이 최소일 때
            -> 이런 애들이 여러 개일 수도 있잖아??
                -> 아예 함수로 빼자!
                    다 채워진 visited를 들고, 우선 sea 배열에서 baby보다 작은 애들을 전부 찾아
                        -> 이 좌표 리스트 중에 visited의 값이 가장 작은 애들을 i, j 값을 넣어서 bfs로 쏴줘
                        근데 재귀가 안 되게 하려면
                        메인
                        bfs()
                        feed_baby()
                        이런 식으로 굴려야 되는데, 얘네가 끝나는 조건은?
                        더이상 먹을 게 없을 때임 그럼 메인에다가 맨 처음 for문 설정을 0 제외 먹이 갯수로 하고
                        저 두 개 돌고 나오면 다시 그 안에 for문 써서 먹을 수 있는 남은 먹이 개수 세서 빼주는 while문
                            -> 그렇게 해서 저 먹을 수 있는 먹이 개수가 0이 되면 while문 종료, print
                해당 (ci, cj)가 si, sj가 되는 거고, total += visited[ci][cj]를 해주면 됨
'''
from collections import deque

def oob(i, j):
    return 0<=i<N and 0<=j<N and sea[i][j] <= baby


def feed_baby(visited):
    global total, cnt, baby

    tmp = []
    for i in range(N):
        for j in range(N):
            if sea[i][j] < baby and sea[i][j] != 0 and visited[i][j] != 0:
                tmp.append((visited[i][j], i, j))

    if not tmp:
        for i in range(N):
            for j in range(N):
                sea[i][j] = 0
        return

    tmp.sort()  # 그러면 baby가 먹을 수 있는 물고기 중 현재 위치에서 가장 가까운 녀석이 [0]으로 옴
    # 거리가 같더라도 i, j 순으로 정렬해서 가능
    num, i, j = tmp[0]
    total += num-1  # 시간을 더해줌
    cnt += 1

    if cnt == baby:
        baby += 1
        cnt = 0

    sea[i][j] = 9  # 아기상어의 현재 위치로 바꿔 줌
    return


def bfs(si, sj):
    q = deque()
    visited[si][sj] = 1
    q.append((si, sj))
    sea[si][sj] = 0

    while q:
        ci, cj = q.popleft()
        for di, dj in dir:
            ni, nj = ci+di, cj+dj
            if oob(ni, nj) and visited[ni][nj] == 0:
                visited[ni][nj] = visited[ci][cj] + 1
                q.append((ni, nj))

    return


N = int(input())
sea = [list(map(int, input().split())) for _ in range(N)]
total = 0
dir = [(0, 1), (0, -1), (1, 0), (-1, 0)]
baby = 2

feed = N*N
tmp, cnt = 0, 0
# 먹이가 남아있는 동안 이 두 가지를 돌고, edible한 feed가 없으면 종료
# 더이상 lst에 담을 수 없을 때, 모든 배열을 0으로 바꿔주기

si, sj = 0, 0
while feed > 0:
    visited = [[0]*N for _ in range(N)]

    for i in range(N):
        for j in range(N):
            if sea[i][j] == 9:
                si, sj = i, j

    bfs(si, sj)
    feed_baby(visited)
    tmp = 0
    for i in range(N):
        for j in range(N):
            if sea[i][j] != 0 and sea[i][j] != 9:  # 남은 순수 먹이 갯수 .. 먹을 수 있는
                tmp += 1
    feed = tmp

print(total)