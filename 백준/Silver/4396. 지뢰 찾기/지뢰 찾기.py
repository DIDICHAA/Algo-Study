def noob(i, j):
    return 0<=i<N and 0<=j<N


def check_no_bomb():
    for i in range(N):
        for j in range(N):
            if bomb[i][j] == '.' and play[i][j] == 'x':
                cnt = 0
                for di, dj in DIR:
                    ni, nj = i+di, j+dj
                    if noob(ni, nj) and bomb[ni][nj] == '*':
                        cnt += 1
                arr[i][j] = cnt
    return


def check_bomb():
    flag = False
    for i in range(N):
        for j in range(N):
            if bomb[i][j] == '*' and play[i][j] == 'x':
                flag = True

    if flag:
        for i in range(N):
            for j in range(N):
                if bomb[i][j] == '*':
                    arr[i][j] = '*'
    return


N = int(input())
bomb = [list(map(str, input().strip())) for _ in range(N)]
play = [list(map(str, input().strip())) for _ in range(N)]
arr = [['.' for _ in range(N)] for _ in range(N)]
DIR = [(-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1)]

# 지뢰가 없으면서 열린 칸은 8방 지뢰갯수에 맞게 0~8
# 지뢰가 있는 칸이 열렸다면 지뢰가 있는 모든 칸이 *표시

check_no_bomb()
check_bomb()
for lst in arr:
    for n in lst:
        print(n, end="")
    print()