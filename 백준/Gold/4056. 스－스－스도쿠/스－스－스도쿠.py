def check(arr):
    for x, y in candidate:
        check_set = set()

        for i in range(9):
            if arr[i][y] in check_set:
                return False
            check_set.add(arr[i][y])

        check_set = set()
        for j in range(9):
            if arr[x][j] in check_set:
                return False
            check_set.add(arr[x][j])

    for i in range(0, 9, 3):
        for j in range(0, 9, 3):
            tmp_board = [lst[j:j+3] for lst in arr[i:i+3]]
            check_set = set()
            for r in range(3):
                for c in range(3):
                    if tmp_board[r][c] in check_set:
                        return False
                    check_set.add(tmp_board[r][c])
    return True


def dfs(cnt, lst):
    global flag, board

    if cnt == len(candidate):
        tmp_board = [row[:] for row in board]
        for n in range(len(lst)):
            x, y = candidate[n]
            num = lst[n]
            tmp_board[x][y] = num
        if check(tmp_board):
            board = tmp_board
            flag = True
            return
        return

    for i in range(9):
        lst.append(nums[i])
        dfs(cnt+1, lst)
        lst.pop()


T = int(input())
for tc in range(1, T+1):
    board = [list(map(int, input())) for _ in range(9)]

    nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    candidate = []
    for i in range(9):
        for j in range(9):
            if board[i][j] != 0: continue
            candidate.append([i, j])

    flag = False
    dfs(0, [])

    if flag:
        for lst in board:
            for n in lst:
                print(n, end='')
            print()
    else:
        print("Could not complete this grid.")
    if tc != T:
        print()