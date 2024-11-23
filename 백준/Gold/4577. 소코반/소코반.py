def iob(i, j):
    return 0<=i<R and 0<=j<C


def move():
    di, dj = DIR_DICT[command]
    ni, nj = si+di, sj+dj
    if not iob(ni, nj) or board[ni][nj] == '#':
        return

    # condition 1 - if toward is a box
    if board[ni][nj] in 'bB':
        nni, nnj = ni+di, nj+dj

        if not iob(nni, nnj) or board[nni][nnj] in '#bB':
            return

        # box on the ground
        if board[ni][nj] == 'b':
            if board[nni][nnj] == '.':
                board[nni][nnj] = 'b'
                board[ni][nj] = 'w'
                board[si][sj] = origin[si][sj]

            # approach to goal
            else:
                board[nni][nnj] = 'B'
                board[ni][nj] = 'w'
                board[si][sj] = origin[si][sj]

        # box on the goal
        else:
            if board[nni][nnj] == '.':
                board[nni][nnj] = 'b'
                board[ni][nj] = 'W'
                board[si][sj] = origin[si][sj]

            # approach to goal
            else:
                board[nni][nnj] = 'B'
                board[ni][nj] = 'W'
                board[si][sj] = origin[si][sj]

    # condition 2 - if toward is ground
    elif board[ni][nj] == '.':
        board[ni][nj] = 'w'
        board[si][sj] = origin[si][sj]

    # condition 3 - if toward is goal
    else:
        board[ni][nj] = 'W'
        board[si][sj] = origin[si][sj]

    return


def check():
    for i in range(R):
        for j in range(C):
            if origin[i][j] != '+': continue
            if board[i][j] == 'B': continue
            return False
    return True


def find_start():
    for i in range(R):
        for j in range(C):
            if board[i][j] == 'w' or board[i][j] == 'W':
                return i, j

tc = 1
while 1:
    R, C = map(int, input().split())
    if (R, C) == (0, 0):
        break
    origin = [list(map(str, input())) for _ in range(R)]
    board = [lst[:] for lst in origin]
    for i in range(R):
        for j in range(C):
            if origin[i][j] in 'BW':
                origin[i][j] = '+'
            elif origin[i][j] in 'bw':
                origin[i][j] = '.'
    commands = list(map(str, input()))
    DIR_DICT = {'U':(-1, 0), 'L':(0, -1), 'D':(1, 0), 'R':(0, 1)}

    flag = False
    for command in commands:
        si, sj = find_start()
        move()
        if check():
            flag = True
            break

    if flag:
        print(f'Game {tc}: complete')
    else:
        print(f'Game {tc}: incomplete')
    for lst in board:
        print(''.join(lst))
    tc += 1