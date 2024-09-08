'''
2124 문제 이해)
전체 파이어스톰 크기는 2^n * 2^n
격자 나누는 크기는 2^l * 2^l // l이 커질 수록 회전시키는 범위가 커지는 거임
    -> 함수화
이 모든 부분 격자를 시계 방향으로 90도 회전 !!
이후, 사방에 얼음이 있는 칸이 3개 이상이 아니라면 얼음 양 -= 1
    -> 함수화

남아있는 얼음의 합, 남아있는 얼음 중 가장 큰 덩어리가 차지하는 칸의 개수(bfs max 갱신)

2128
~ 여기서부터 구상 및 설계~
[ 주어진 l에 따라 배열 돌리는 함수 ]

[ 사방에 얼음 3개 이상인지 체크하고 얼음 양 없애는 함수 ]

[ 최종적으로 얼음 덩어리 체크 할 bfs 함수 ]

[ main ]

2209 디버깅
1. 전체 Ice의 값이 미묘하게 다르다 ...
    -> 배열 잘 돌아갔나요?
        => 아니!! 맨 마지막 애들이 안 돌아갔다 range 설정 잘못되었음을 직감
            => 해결
2. 2번 테케부터 값이 안 맞음 / 더 크게 나오는 걸로 봐서는 사라져야 할 얼음들이 사라지지 못했다
    -> 여기서의 의문 ... 0이 있어야만 얼음이 사라지는데 초기 배열이 죄다 수가 있는데 어케 사라지지?
    ** 내가 문제에서 잡아내지 못한 얼음 사라지는 조건이 있을 것 ** 나를 끝없이 의심해라 **
        => '이후 얼음이 있는 칸 3개 또는 그 이상과 인접해있지 않은 칸은 얼음의 양이 1 줄어든다.'
            => oob 되는 부분 cnt 따로 세서 처리 완료

3. 4번 테케부터 값이 이상함 .. 그냥 이상함
    -> 후... cnt, o_cnt의 값을 더했을 떄 이게 2개 이상이면 무조건 얼음 사라져야 함

'''
from collections import deque
def oob(i, j):
    return 0<=i<N and 0<=j<N


def check_maxice(si, sj):
    global maxi

    q = deque()
    visited[si][sj] = 1
    q.append((si, sj))

    cnt = 1  # 첫 칸도 포함해서 세줘야 하니까
    while q:
        ci, cj = q.popleft()
        for di, dj in dir:
            ni, nj = ci+di, cj+dj
            if oob(ni, nj) and visited[ni][nj] == 0 and ice[ni][nj] != 0:
                visited[ni][nj] = 1
                q.append((ni, nj))
                cnt += 1

    maxi = max(maxi, cnt)
    return


def check_ice():

    grids = []
    for i in range(N):
        for j in range(N):
            cnt = 0
            o_cnt = 0
            for di, dj in dir:
                ni, nj = i+di, j+dj
                if oob(ni, nj) and ice[ni][nj] == 0:
                    cnt += 1
                if not oob(ni, nj):  # oob로 빠지는 애들은 2개 이상 빠져야만 모서리에 있는 애들이라 ... 1개 이상이면 극변 값들이 다 빠짐
                    o_cnt += 1

            if (cnt + o_cnt >= 2) and ice[i][j] > 0:  # 사방 중 얼음이 없는 곳이 한 군데 이상이라면
                grids.append((i, j))
            # elif o_cnt >= 2 and ice[i][j] > 0:
            #     grids.append((i, j))  # 후... 모아놨다가 한 번에 빼줘야 함

    # print(*ice, sep='\n')
    # print('-----------바꾸기 전-----------')

    for x, y in grids:
        ice[x][y] -= 1

    # print(*ice, sep='\n')
    # print('###########################')
    return

def rotate_ice(L):
    # 2^L 사이즈로 ice를 가른 뒤, 시계 방향으로 90도 회전
    # 부분 배열 돌리기 레츠고
    l = 2**L
    tmp = []
    for i in range(0, N-l+1, l):
        for j in range(0, N-l+1, l):
            tmp = [x[j:j+l] for x in ice[i:i+l]]
            tmp = list(map(list, zip(*tmp[::-1])))

            for x in range(l):
                ice[i+x][j:j+l] = tmp[x]

    return


n, Q = map(int, input().split())
N = 2**n
ice = [list(map(int, input().split())) for _ in range(N)]
commands = list(map(int, input().split()))
dir = [(0, 1), (0, -1), (1, 0), (-1, 0)]
visited = [[0]*N for _ in range(N)]

for command in commands:
    rotate_ice(command)
    check_ice()

maxi = 0
for i in range(N):
    for j in range(N):
        if ice[i][j] != 0 and visited[i][j] == 0:
            check_maxice(i, j)

tmp = sum(ice, [])
ans = sum(tmp)
print(ans, maxi, end='\n')