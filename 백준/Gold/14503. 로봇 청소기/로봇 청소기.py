'''
동서남북 중 하나의 방향 - 좌표는 (0, 0)부터 표준대로 움직임

1. 현재 칸이 아직 청소되지 않은 경우, 현재 칸을 청소한다.
2. 현재 칸의 주변 4칸 중 청소되지 않은 빈 칸이 없는 경우,
    1. 바라보는 방향을 유지한 채로 한 칸 후진할 수 있다면 한 칸 후진하고 1번으로 돌아간다.
    2. 바라보는 방향의 뒤쪽 칸이 벽이라 후진할 수 없다면 작동을 멈춘다.
3. 현재 칸의 주변 4칸 중 청소되지 않은 빈 칸이 있는 경우,
    1. 반시계 방향으로 90도 회전한다.
    2. 바라보는 방향을 기준으로 앞쪽 칸이 청소되지 않은 빈 칸인 경우 한 칸 전진한다.
    3. 1번으로 돌아간다

위 그대로 구현하기 .. !
dir 북동남서 0123

[ 디버깅 리스트 ]
1. 어딘가에서 나의 로봇 청소기가 무한히 돌고 있다
    -> ni, nj에서 오타가 남
2. 청소를 깔끔하게 하지 못하는 이슈가 발생함
    -> 청소 관련 ==1이냐 ==2냐 에서 아마 오류가 난 거 같음
        => 은 아니라서 문제에 숨겨져있는 Return 조건을 더 세밀하게 따져봐야 할 듯
    -> 로봇 청소기가 청소를 하다가 멈춤;

'''


def oob(i, j):
    return 0 <= i < N and 0 <= j < M


def clean_room(i, j, d):
    if room[i][j] == 0:
        room[i][j] = 2  # 청소한 칸은 2로 채워주자!

    flag = True

    for di, dj in dir:
        ni, nj = i+di, j+dj

        if oob(ni, nj):
            if room[ni][nj] == 0:
                flag = False
                break

    if not flag:  # 한 군데라도 청소가 안 돼 있다면
        d = (d-1) % 4
        x, y = dir[d]
        ci, cj = i+x, j+y
        if oob(ci, cj) and room[ci][cj] == 0:
            i, j = ci, cj

        # else의 경우에는 어떻게 되는 거죠
    else:  # 4군데 모두 청소가 돼 있다면
        x, y = dir[d]
        ci, cj = i-x, j-y
        if oob(ci, cj):
            if room[ci][cj] != 1:
                i, j = ci, cj
            else:
                return i, j, d, -1

    return i, j, d, 0


N, M = map(int, input().split())
x, y, d = map(int, input().split())
room = [list(map(int, input().split())) for _ in range(N)]
dir = [(-1, 0), (0, 1), (1, 0), (0, -1)]

while True:
    i, j, nd, now = clean_room(x, y, d)
    if now == -1:
        break

    x, y = i, j
    d = nd

tmp = sum(room, [])
ans = tmp.count(2)
print(ans)