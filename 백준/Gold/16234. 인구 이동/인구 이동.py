'''
문제 이해)
국경선을 공유하는 두 나라의 인구 차이가 L ~ R이라면,
국경선 오픈 -> 인구 이동 시작
인접한 칸만을 이용해 인구 이동이 가능하다면 = 해당 나라는 연합
연합을 이루고 있는 각 칸의 인구수 = 연합의 인구수 / 연합의 칸 개수 // int
연합 해체, 국경선 close 의 시퀀스

인구 이동이 더이상 이루어 질 수 없는 조건?
인접국들의 인구 차이가 L명 미만이 될 때 // R명 이상은 발생할 수 없음

구상)
결귝 bfs로 도달할 수 있는 범위라면 ((ci, cj)와 (ni, nj)의 차이가 L이상 R이하)
visited = True 처리된 곳은 모두 더한 뒤, True의 갯수를 센 만큼 나눈 값을
해당 하는 좌표 값에다가 (원본 arr) 업데이트 해준 뒤, bfs 반복

끝나는 지점은 이중 for 문 돌면서 전체 지도 안에서 인접 국들 간의 인구 수 차이가
L 미만이 되었을 때 return
-> 인접국 간의 인구수 계산하는 함수

[ 인접국 간의 인구수 차 계산하는 for문 함수]
[ 연합국의 개수와 인구수를 세어 나누고 update 해주는 함수 ]
[ bfs 함수 ]
[ main ]

구현) 1509 ~
간과한 부분 ~.~ : 영역이 ni, nj / ci, cj 이렇게 두 개가 아니라 여러 개이므로
cal ~ update에 넘겨주는 좌표값들은 전부 리스트에 담겨 있어야 하고
이걸 하나씩 빼서 해당 좌표 안의 값들을 가지고 update 해줘야 함

디버깅) 1530
이슈1.
또!!!!!!!!!!!!!! index range error
-> ㅎㅎ . people 입력을 한 줄만 받아서 ...

이슈2.
테케 4, 5번이 이상한 값이 나온다 ...  사람이 증식하기 시작함 저출산 시댄데
테케 4번의 경우 .. 2번까지 돌았을 때 (2, 1)에 위치한 좌표값이 set()에 안 들어가는 문제 발생
-> 아마도 해당 좌표가 이전 좌표값 기준으로 L~R만큼 차이는 안 나고, visited처리는 되어서 추가적으로 안 돌아간 느낌
-> 어떻게 해결해야 할까? bfs 돌리는 걸 매 좌표로 ..? 해야 할 거 같은데
-> 연합에 속하지 못한 나라들을 대상으로 한 번 더 bfs를 돌릴 수 있는 기회를 줘야만 함

? 지금처럼 모든 지점에서 bfs를 돌려야 할 때 ci, cj처리를 어떻게 해줘야 하는지
? visited를 안 쓸 때에는 return 지점을 어떻게 잡아줘야 하는지
ㅋㅋ tlqkf 고치다가 그냥 테케 하나도 안 맞는 코드 됨
진짜 레전드
?

'''
from collections import deque

def update_people(yeonhap):
    global move_cnts, flag

    tot = 0
    cnts = len(yeonhap)
    if cnts > 1:
        flag = True
        for i, j in yeonhap:
            tot += people[i][j]

        tot = int(tot/cnts)
        for i, j in yeonhap:
            people[i][j] = tot


def cal_people(i, j, ni, nj):
    global yeonhap

    num = abs(people[i][j] - people[ni][nj])

    if L<=num<=R:
        return 1
    else:
        return 0


def bfs(ci, cj):
    global yeonhap

    q = deque()
    yeonhap.append((ci, cj))

    visited[ci][cj] = True
    q.append((ci, cj))

    while q:
        ci, cj = q.popleft()

        for di, dj in dir:
            ni, nj = ci+di, cj+dj
            if 0 <= ni < N and 0 <= nj < N:
                if not visited[ni][nj]:
                    tmp = cal_people(ci, cj, ni, nj)  # 여기서 방문 가능한 노드인지 확인하기 위해 함수 탐색 먼저
                    if tmp == 1:
                        visited[ni][nj] = True
                        q.append((ni, nj))
                        yeonhap.append((ni, nj))


N, L, R = map(int, input().split())
people = [list(map(int, input().split())) for _ in range(N)]
dir = [(0, 1), (0, -1), (1, 0), (-1, 0)]
move_cnts = 0

while True:
    visited = [[False] * N for _ in range(N)]
    flag = False
    for i in range(N):
        for j in range(N):
            yeonhap = []
            if not visited[i][j]:
                bfs(i, j)
                update_people(yeonhap)
    if not flag:
        break
    move_cnts += 1


print(move_cnts)