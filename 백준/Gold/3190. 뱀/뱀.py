'''
[ 마음 가짐 ]
** 문제에서 요구하는 대로 구현하기 **
** 뇌피셜로 해석하기 금지 **
** 인덱스 주의하기 **

1654 문제 이해
0,0 에서 뱀 시작, 뱀 길이는 1, 처음 dir는 오른쪽
머리를 다음 칸에 위치 -> 이동한 칸에 사과 O -> 사과 없어지고 꼬리 그대로
                -> 이동한 칸에 사과 X -> 꼬리칸을 없애줌
출력 : 몇 초에 이 게임이 끝나는가 ??

1655 구상
2차원 배열로 선언 함수로 뱀 움직이면서 머리 위치에 사과 있는 지 확인하기
나머지는 문제에서 주어진 그대로 구현하기

1656 구현
1706 main 잘 돌아가는 거 확인
1750 디버깅 이슈
1. 두 번째 테케에서 꼬리값이 제대로 갱신이 안 되는 거 같음 없어져야 하는데 없어지질 안흠.
1816
2. queue에서 pop을 잘못해주고 있는 듯
-> appendleft 를 안 해줘서 틀렸음!

'''
from collections import deque


def oob(i, j):
    return 0<=i<N and 0<=j<N


def move_snake():
    global game, flag

    hi, hj = snake.popleft()
    di, dj = dir[now]
    ni, nj = hi+di, hj+dj

    # 벽이랑 부딪혀도 안 됨
    if not oob(ni, nj):
        flag = False
        return
    # 자기 몸이랑 부딪혀도 안 됨
    if game[ni][nj] == 1:
        flag = False
        return

    if game[ni][nj] == 2:  # 앞 칸에 사과가 있을 때
        game[ni][nj] = 1  # 해당 칸에 머리 위치, 이 떄는 꼬리 위치 안 바뀜
        snake.appendleft((hi, hj))
        snake.appendleft((ni, nj))

    elif game[ni][nj] == 0:  # 앞 칸에 사과가 없을 때
        if len(snake) > 0:
            ti, tj = snake.pop()
            game[ti][tj] = 0   # 꼬리 위치를 사라지게 함 ..
            snake.appendleft((hi, hj))
        else:
            game[hi][hj] = 0
        snake.appendleft((ni, nj))
        game[ni][nj] = 1

    return


N = int(input())
game = [[0]*N for _ in range(N)]

si, sj = 0, 0  # 머리 위치

game[si][sj] = 1
snake = deque()
snake.append((si, sj))

K = int(input())
for _ in range(K):
    r, c = map(int, input().split())
    game[r-1][c-1] = 2  # 사과는 2

L = int(input())
commands = [list(map(str, input().split())) for _ in range(L)]  # 나중에 앞 X는 정수 변환 잊지 말기
dir = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # 우하좌상 순서

now = 0  # 현재 바라보고 있는 방향은 오른쪽
cnt = 0
flag = True
while flag:
    for second, direction in commands:
        if not flag:
            break
        second = int(second)
        while second != cnt:
            cnt += 1
            move_snake()

            if not flag:
                break

            if cnt == second:
                if direction == 'L':
                    now = (now-1)%4
                else:
                    now = (now+1)%4
                break

print(cnt)