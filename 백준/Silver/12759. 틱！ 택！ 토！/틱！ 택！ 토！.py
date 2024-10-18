def check_i():
    i = 0
    while i < 3:
        if board[i][0] == board[i][1] == board[i][2] == num:
            return True
        i += 1
    return False


def check_j():
    j = 0
    while j < 3:
        if board[0][j] == board[1][j] == board[2][j] == num:
            return True
        j += 1
    return False


def check_c():
    if board[0][0] == board[1][1] == board[2][2] == num:
        return True
    elif board[2][0] == board[1][1] == board[0][2] == num:
        return True
    return False


def change():
    global num

    if num == 1: num = 2
    else:
        num = 1
    return


board = [[0 for _ in range(3)] for _ in range(3)]
num = int(input())
flag = False
for _ in range(9):
    x, y = map(lambda x:int(x)-1, input().split())
    board[x][y] = num
    if check_i() or check_j() or check_c():
        flag = True
        break
    change()

if flag:
    print(num)
else:
    print(0)