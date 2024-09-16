'''
2045 문제 이해)
반지름이 1, 2, ... N인 원판이 있다
크기가 작아지는 순으로 바닥에 놓여 있고, 원판의 중심으 ㄴ모두 같다

원판의 반지름이 i라면 그 원판을 i번째 원판이라고 함
각각의 원판에는 M개의 정수가 적혀있고, i번째의 원판에 적힌 j번째 수의 위치는 (i, j)로 표시

(i, 1)은 (i, 2), (i, M)과 인접하다.
(i, M)은 (i, M-1), (i, 1)과 인접하다.
(i, j)는 (i, j-1), (i, j+1)과 인접하다. (2 ≤ j ≤ M-1)
(1, j)는 (2, j)와 인접하다.
(N, j)는 (N-1, j)와 인접하다.
(i, j)는 (i-1, j), (i+1, j)와 인접하다. (2 ≤ i ≤ N-1)

2103 구상)
주어진 x는 그에 배수에 준하는 원판들은 다 돌려야 됨
시계 or 반시계 방향으로 몇 칸 회전 시키냐 // 각각 함수 구현
0은 시계, 1은 반시계
원판에 수가 남아 있다면 인접하면서 같은 수인 걸 모두 찾은 뒤, 지워줌
없으면 원판에 적힌 수의 평균을 구하고, 평균보다 큰 수는 -=1, 작은 수는 += 1을 해줌
지워줄 떄는 0으로 대체해주고 평균 구할 때만 유의해주면 될 거 같네요

2107 구현
2137 디버깅
이슈 1. 테케 4~5가 값이 안 맞음 원판 까봐야 할 거 같당 아마 수가 제대로 안 없어지지 않았을까?
    -> 양 끝단 처리를 안 해줘서 숫자가 안 없어졌엉
'''
def rotate_clockwise(x, k):
    x_lst = [n-1 for n in range(x, N+1, x)]
    # x의 배수에 준하는 원판을 +k씩 돌려줘야 합니다 ...
    for i in x_lst:
        tmp = [0] * M
        for j in range(M):
            tmp_k = (j+k) % M  # tmp에 넣어줄 자릿값...
            tmp[tmp_k] = wonpan[i][j]
        wonpan[i] = tmp

    return

def rotate_counterclock(x, k):
    x_lst = [n-1 for n in range(x, N+1, x)]
    # x의 배수에 준하는 원판을 +k씩 돌려줘야 합니다 ...
    for i in x_lst:
        tmp = [0] * M
        for j in range(M):
            tmp_k = (j-k) % M  # tmp에 넣어줄 자릿값...
            tmp[tmp_k] = wonpan[i][j]
        wonpan[i] = tmp

    return


def find_nums():
    flag = False
    t_won = sum(wonpan, [])
    num = t_won.count(0)

    if num != N*M:
        tmp = set()
        for i in range(N):
            for j in range(1, M):
                if wonpan[i][j] != 0:
                    if wonpan[i][j] == wonpan[i][j-1]:
                        tmp.add((i, j-1))
                        tmp.add((i, j))
                if wonpan[i][0] != 0 and wonpan[i][0] == wonpan[i][-1]:
                    tmp.add((i, 0))
                    tmp.add((i, M-1))

        for j in range(M):
            for i in range(1, N):
                if wonpan[i][j] != 0:
                    if wonpan[i][j] == wonpan[i-1][j]:
                        tmp.add((i-1, j))
                        tmp.add((i, j))

        for x, y in tmp:
            wonpan[x][y] = 0
            flag = True

    # 원판에 수가 하나도 없었을 때만
        if not flag:
            t_avg = 0
            t_cnt = 0
            for i in range(N):
                for j in range(M):
                    if wonpan[i][j] != 0:
                        t_avg += wonpan[i][j]
                        t_cnt += 1
            t_avg /= t_cnt
            for i in range(N):
                for j in range(M):
                    if wonpan[i][j] != 0:
                        if wonpan[i][j] > t_avg:
                            wonpan[i][j] -= 1
                        elif wonpan[i][j] < t_avg:
                            wonpan[i][j] += 1
    return


N, M, T = map(int, input().split())
wonpan = [list(map(int, input().split())) for _ in range(N)]

for tc in range(T):
    x, d, k = map(int, input().split())
    if d == 0:
        rotate_clockwise(x, k)
    else:
        rotate_counterclock(x, k)

    find_nums()

tmp = sum(wonpan, [])
ans = sum(tmp)
print(ans)