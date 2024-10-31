'''
1. 종수가 아두이노를 8방으로 이동시키거나, 그 위치에 그대로 둠

2. 종수의 아두이노가 미친 아두이노가 있는 칸으로 이동 시,
    - 게임 종료 / 종수가 짐

3. 미친 아두이노는 8방 중 종수의 아두이노와 가장 가까워지는 방향으로 한 칸 이동
    - 맨해탄 거리가 가장 작아지는 방향으로 이동함

4. 미친 아두이노가 종수의 아두이노가 있는 칸으로 이동 시,
    - 게임 종료 / 종수가 짐

5. 2개 또는 그 이상의 미친 아두이노가 같은 칸에 있을 시, 큰 폭발 발생
    -> 그 칸에 있는 아두이노 모두 파괴

'''
def noob(i, j):
    return 0<=i<R and 0<=j<C


def find_js():
    for i in range(R):
        for j in range(C):
            if board[i][j] == 'I':
                return i, j


def find_ca():
    lst = []
    for i in range(R):
        for j in range(C):
            if board[i][j] == 'R':
                lst.append([i, j])

    return lst


def move_js():
    di, dj = DIR[command]
    si, sj = find_js()
    ni, nj = si+di, sj+dj
    if noob(ni, nj):
        if board[ni][nj] == 'R':
            return False  # 미친 아두이노가 있는 칸일 때
        else:
            board[si][sj] = '.'
            board[ni][nj] = 'I'
    return True


def move_ca():
    total_tmp = [[[] for _ in range(C)] for _ in range(R)]

    ji, jj = find_js()
    crazy_lst = find_ca()
    for x, y in crazy_lst:
        tmp = []
        for di, dj in DIR:
            ni, nj = x+di, y+dj
            if noob(ni, nj):
                t_dis = abs(ji-ni) + abs(jj-nj)
                tmp.append([t_dis, ni, nj])
        tmp.sort()
        _, nni, nnj = tmp[0]
        if board[nni][nnj] == 'I':
            return False  # 움직이려는 칸에 종수가 있으면 끝
        total_tmp[nni][nnj].append([x, y])

    remove = []
    add = []
    for i in range(R):
        for j in range(C):
            if not total_tmp[i][j]: continue
            if len(total_tmp[i][j]) == 1:
                x, y = total_tmp[i][j][0]
                remove.append([x, y])
                add.append([i, j])
            else:
                for k in range(len(total_tmp[i][j])):
                    x, y = total_tmp[i][j][k]
                    remove.append([x, y])
    for x, y in remove:
        board[x][y] = '.'
    for xx, yy in add:
        board[xx][yy] = 'R'

    return True


R, C = map(int, input().split())
board = [list(map(str, input().strip())) for _ in range(R)]
commands = list(map(lambda x:int(x)-1, input().strip()))
DIR = [(1, -1), (1, 0), (1, 1), (0, -1), (0, 0), (0, 1), (-1, -1), (-1, 0), (-1, 1)]
crazy = [[[] for _ in range(C)] for _ in range(R)]
flag = False
time = 1
for command in commands:
    if not move_js():
        flag = True
        break

    if not move_ca():
        flag = True
        break
    time += 1

if flag:
    print(f"kraj {time}")
else:
    for lst in board:
        for n in lst:
            print(n, end="")
        print()