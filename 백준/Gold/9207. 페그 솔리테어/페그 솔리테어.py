def iob(i, j):
    return 0<=i<5 and 0<=j<9


def dfs(arr, cnt):
    tmp_arr = [lst[:] for lst in arr]

    for i in range(5):
        for j in range(9):
            if arr[i][j] != 'o': continue
            for d in range(4):
                di, dj = DIR[d]
                ni, nj = i+di, j+dj
                if not iob(ni, nj): continue
                if arr[ni][nj] != 'o': continue
                nni, nnj = ni+di, nj+dj
                if not iob(nni, nnj): continue
                if arr[nni][nnj] != '.': continue
                # 이동 처리 해주기
                arr[i][j], arr[ni][nj] = '.', '.'
                nni, nnj = ni + di, nj + dj
                arr[nni][nnj] = 'o'

                dfs(arr, cnt+1)
                arr = [lst[:] for lst in tmp_arr]

    lst = [sum(arr, []).count('o'), cnt]
    result.append(lst)
    return


T = int(input())
for tc in range(T):
    board = [list(map(str, input())) for _ in range(5)]
    if tc != T-1:
        _ = input()

    result = []
    DIR = [(-1, 0), (0, 1), (1, 0), (0, -1)]

    dfs(board, 0)

    if not result:
        print(sum(board, []).count('o'), 0)
    else:
        print(*min(result))
