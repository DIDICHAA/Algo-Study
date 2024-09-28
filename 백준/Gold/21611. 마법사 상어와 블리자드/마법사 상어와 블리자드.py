'''
** 문제 이해 완벽하게 하고 풀기 **
** 문제에서 주어진 순서대로 구현하기 **
** 함수 내 조건 분기 확실하게 하기 - 불안하면 주석 달기 **
** 함수 별 유닛 테스트 확인하고 넘어가기 / 배열 다 까보기 **

2200 문제 이해

1. 가장 처음 상어가 있는 칸을 제외한 나머지 칸에는 구슬이 하나 들어갈 수 있음
    - 같은 번호를 가진 구슬이, 번호가 연속하는 칸에 있으면 연속하는 구슬

2. 방향은 상하좌우 순서 1, 2, 3, 4로 주어짐 - 1번 함수
    - d방향으로 거리가 s이하인 모든 칸에 얼음 파편을 던져 그 칸에 있는 구슬 모두 파괴
    - 구슬 파괴 시, 그 칸은 구슬이 없는 빈 칸이 됨

3. 만약 어떤 칸 A의 번호보다 하나 작은 칸이 빈 칸이면, (연쇄 이동) - 2번 함수
    - A에 있는 구슬은 그 빈 칸으로 이동
    - 더이상 구슬이 이동하지 않을 때까지 반복

4. 구슬 폭발 - 3번 함수
    - 4개 이상 연속하는 구슬이 있을 시 발생 (0으로 처리해주기)
    - 다시 3번의 연쇄 이동 - 4번 (반복) // flag 세워서 return 해줘서 확인하기
        -> 더이상 폭발하는 구슬이 없을 때까지 반복

5. 구슬 변화 - 4번 함수
    - 연속하는 구슬은 하나의 그룹 (1개짜리도 포함)
    - 하나의 그룹은 두 개의 구슬 A, B로 변함.
        - 구슬 A의 번호는 그룹에 들어있는 구슬의 개수,
        - B는 그 그룹을 이루고 있는 구슬의 번호
        - 구슬은 그룹의 순서대로 1번 칸부터 차례대로 A, B의 순서대로 들어감
            -> 만약 구슬이 칸의 개수보다 많아서 다 못들어가면 그 구슬은 사라짐

출력 : 1 * (폭발한 1번 구슬의 개수) + 2 *(폭발한 2번 구슬의 개수) + 3 * (폭발한 3번 구슬의 개수)
-> exploded = [0] * 4 해서 1, 2, 3인덱스 값 더해주기
** 순서대로 구현하기. 차분하게! **
** 함수별로 확인 꼭 하기. 수나 방향 등 어림짐작으로 넘어가지 말기 **
'''
from collections import deque

def noob(i, j):
    return 0<=i<N and 0<=j<N

def make_snail():
    snail_DIR = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    visited = [[False for _ in range(N)] for _ in range(N)]
    d = 0
    visited[si][sj] = True
    ni, nj = si, sj-1
    visited[ni][nj] = True  # 1위치까지만 잡아주기
    lst = [[si, sj-1]]
    for num in range(2, N**2):
        di, dj = snail_DIR[d]
        nni, nnj = ni+di, nj+dj
        if noob(nni, nnj) and not visited[nni][nnj]:
            d = (d+1)%4
            visited[nni][nnj] = True
            ni, nj = nni, nnj
            lst.append([nni, nnj])
        else:
            d = (d-1)%4
            di, dj = snail_DIR[d]
            ni, nj = ni+di, nj+dj
            visited[ni][nj] = True
            d = (d+1)%4
            lst.append([ni, nj])
    return lst


def kill_gooseul(d, s):
    '''
    - d방향으로 거리가 s이하인 모든 칸에 얼음 파편을 던져 그 칸에 있는 구슬 모두 파괴
    - 구슬 파괴 시, 그 칸은 구슬이 없는 빈 칸이 됨
    '''
    di, dj = DIR[d]
    for mul in range(1, s+1):
        ni, nj = si+di*mul, sj+dj*mul
        if noob(ni, nj):
            board[ni][nj] = 0
    return


def move_gooseul():
    global board
    '''
    만약 어떤 칸 A의 번호보다 하나 작은 칸이 빈 칸이면, (연쇄 이동) - 2번 함수
    - A에 있는 구슬은 그 빈 칸으로 이동 - 더이상 구슬이 이동하지 않을 때까지 반복
    그냥 board 싸악 돌면서 x, y는 lst순서대로
    0아닌 애들 queue에 싹 집어넣고 빈 임시 배열에다가 하나씩 넣으면 되지 않나
    '''
    q = deque()
    tmp_arr = [[0 for _ in range(N)] for _ in range(N)]

    for x, y in lst:
        if board[x][y] != 0:
            q.append(board[x][y])

    for x, y in lst:
        if q:
            num = q.popleft()
            tmp_arr[x][y] = num
        else:
            break

    board = tmp_arr
    return


def explode_gooseul():
    '''
    - 4개 이상 연속하는 구슬이 있을 시 발생 (0으로 처리해주기)
    - 다시 3번의 연쇄 이동 - 4번 (반복) // flag 세워서 return 해줘서 확인하기
    -> 더이상 폭발하는 구슬이 없을 때까지 반복
    '''
    flag = False  # 한 번이라도 폭발이 일어났는 지 확인해줄 거여
    cnt = 0
    tmp = []
    for i in range(1, len(lst)):
        x, y = lst[i-1]
        num = board[x][y]
        nx, ny = lst[i]
        if board[nx][ny] == num:
            cnt += 1
            tmp.append((x, y))
            tmp.append((nx, ny))
        else:
            if cnt >= 3:
                tmp = list(set(tmp))
                for ni, nj in tmp:
                    num = board[ni][nj]
                    exploded[num] += 1
                    board[ni][nj] = 0
                flag = True
            tmp = []
            cnt = 0
    return flag


def change_gooseul():
    global board

    tmp_arr = [[0 for _ in range(N)] for _ in range(N)]
    n = 0
    q = deque(lst)
    ttmp = []
    while q:
        tmp = []
        x, y = q.popleft()
        num = board[x][y]
        if num == 0:
            break
        tmp.append((x, y))
        while q:
            nx, ny = q.popleft()
            if board[nx][ny] == num:
                tmp.append((nx, ny))
            else:
                q.appendleft((nx, ny))
                break
        cnt = len(tmp)
        ttmp.append([cnt, num])

    tn = 0
    i = 1
    while i < len(lst):
        x, y = lst[i-1]
        nx, ny = lst[i]
        if tn < len(ttmp):
            cnt, num = ttmp[tn]
            tmp_arr[x][y] = cnt
            tmp_arr[nx][ny] = num
            tn += 1
            i += 2
        else:
            break

    board = tmp_arr
    return


N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
DIR = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # 상하좌우 순서
exploded = [0]*(4)
si, sj = N//2, N//2  # 상어의 초기 위치

lst = make_snail()

for _ in range(M):
    d, s = map(int, input().split())
    d -= 1
    kill_gooseul(d, s)
    flag = True
    while flag:
        move_gooseul()
        flag = explode_gooseul()  # 폭발한 구슬이 없을 때 return False
    change_gooseul()

res = 1*(exploded[1]) + 2*(exploded[2]) + 3*(exploded[3])
print(res)