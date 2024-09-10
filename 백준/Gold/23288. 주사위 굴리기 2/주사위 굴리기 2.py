'''
si, sj = 0, 0
dir = 0, 1, 2, 3 / 북동남서
주사위 아랫면에 있는 정수A와, 주사위가 있는 칸에 있는 정수 B를 비교
-> A > B : (dir+1)%4
-> A < B : (dir-1)%4
-> A == B : dir = dir

현재 위치 기준 사방에 정수 B와 같은 수가 있을 시 이동 가능 - bfs 활용
갈 수 있는 칸의 개수 : C
점수는 B*C
출력은 점수의 합

1412 구상
1. 각 면이 굴러갈 때마다 주사위 idx가 어떻게 바뀌는 지를 생각해야 함
    -> 함수로 빼서 만들기
2. 1번 함수에서 빠져나온 main에서 A와 B의 값 비교 후 dir 재설정
    -> main에서 함수를 돌려주는 while문 필요 // 이동하는 횟수로 종료조건 설정
3. 현재 x, y 위치를 si, sj로 잡고, 정수 B와 동일한 수가 있는 사방탐색 bfs
    -> 안에서 cnt 올려주고 이 cnt 값이 C가 됨
4. bfs까지 다 돈 후, B와 C를 곱한 값을 total에다가 더해줌
1414 구현
'''
# 주사위 인덱스를 굴리는 방향에 맞춰 바꿔주는 함수
# ㅎㅎ 주사위 굴리기 어케 풀었었는지 기억이 1나도 안 남
from collections import deque


def oob(i, j):
    return 0<=i<N and 0<=j<M


def move_dice(si, sj, d):
    di, dj = dir[d]
    ci, cj = si+di, sj+dj
    if oob(ci, cj):
        return ci, cj, d
    else:  #이동 방향에 칸이 없다면 이동 방향 반대로 해서 한 칸 굴러가야 함
        d = (d-2)%4
        ddi, ddj = dir[d]
        cci, ccj = si+ddi, sj+ddj
        return cci, ccj, d


def change_idx():
    # 현재 굴러간 방향과 위치를 기반으로
    global bot, fron, up, back, left, right

    if d == 0:
        bot, fron, up, back = back, bot, fron, up
    elif d == 1:
        bot, up, left, right = right, left, bot, up
    elif d == 2:
        bot, fron, up, back = fron, up, back, bot
    else:
        bot, up, left, right = left, right, up, bot


def bfs(si, sj, B):
    visited = [[0]*M for _ in range(N)]
    q = deque()
    visited[si][sj] = 1
    q.append((si, sj))
    cnt = 1

    while q:
        ci, cj = q.popleft()
        for di, dj in dir:
            ni, nj = ci+di, cj+dj
            if oob(ni, nj) and visited[ni][nj] == 0 and jido[ni][nj] == B:
                visited[ni][nj] = 1
                q.append((ni, nj))
                cnt += 1
    return cnt


N, M, K = map(int, input().split())
jido = [list(map(int, input().split())) for _ in range(N)]
dir = [(-1, 0), (0, 1), (1, 0), (0, -1)]  # 북동남서 순서

total = 0
si, sj = 0, 0
d = 1  # 초기 값들 설정
# 주사위 초기 위치 idx값
bot, fron, up, back, left, right = 6, 5, 1, 2, 4, 3
while K > 0:
    ci, cj, d = move_dice(si, sj, d)
    change_idx()

    A = bot
    B = jido[ci][cj]
    if A > B:
        d = (d+1)%4
    elif A < B:
        d = (d-1)%4

    C = bfs(ci, cj, B)
    total += B*C
    si, sj = ci, cj
    K -= 1

print(total)