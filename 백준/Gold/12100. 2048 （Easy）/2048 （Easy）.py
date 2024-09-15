from collections import deque

def simulate(board, d):
    # d 방향으로 board 밀고 그 결과 반환하는 함수
    tmp_board = [[0] * N for _ in range(N)]

    if d == 1:  # 우측으로 움직일 떄
        for i in range(N):
            idx = N - 1
            tmp = deque()
            for j in range(N - 1, -1, -1):
                if board[i][j] != 0:
                    tmp.append(board[i][j])

            if len(tmp) == 0:
                continue
            elif len(tmp) == 1:
                num = tmp.pop()
                tmp_board[i][idx] = num
            else:
                tmp_2 = []
                while tmp:
                    if len(tmp) == 1:
                        num = tmp.pop()
                        tmp_2.append(num)
                        break

                    if tmp[0] != tmp[1]:
                        num = tmp.popleft()
                        tmp_2.append(num)

                    elif tmp[0] == tmp[1]:
                        num = tmp.popleft()
                        tmp_2.append(num * 2)
                        tmp.popleft()  # 같은 숫자 두 개니까 한 번 더 빼줌..

                for n in tmp_2:
                    tmp_board[i][idx] = n
                    idx -= 1

    elif d == 2:  # 하측으로 움직일 떄
        for j in range(N):
            idx = N - 1
            tmp = deque()
            for i in range(N - 1, -1, -1):
                if board[i][j] != 0:
                    tmp.append(board[i][j])

            if len(tmp) == 0:
                continue
            elif len(tmp) == 1:
                num = tmp.pop()
                tmp_board[idx][j] = num
            else:
                tmp_2 = []
                while tmp:
                    if len(tmp) == 1:
                        num = tmp.pop()
                        tmp_2.append(num)
                        break

                    if tmp[0] != tmp[1]:
                        num = tmp.popleft()
                        tmp_2.append(num)

                    elif tmp[0] == tmp[1]:
                        num = tmp.popleft()
                        tmp_2.append(num * 2)
                        tmp.popleft()

                for n in tmp_2:
                    tmp_board[idx][j] = n
                    idx -= 1

    elif d == 3:  # 좌측으로 움직일 떄
        for i in range(N):
            idx = 0
            tmp = deque()
            for j in range(N):
                if board[i][j] != 0:
                    tmp.append(board[i][j])

            if len(tmp) == 0:
                continue
            elif len(tmp) == 1:
                num = tmp.pop()
                tmp_board[i][idx] = num
            else:
                tmp_2 = []
                while tmp:
                    if len(tmp) == 1:
                        num = tmp.pop()
                        tmp_2.append(num)
                        break

                    if tmp[0] != tmp[1]:
                        num = tmp.popleft()
                        tmp_2.append(num)

                    elif tmp[0] == tmp[1]:
                        num = tmp.popleft()
                        tmp_2.append(num * 2)
                        tmp.popleft()  # 같은 숫자 두 개니까 한 번 더 빼줌..

                for n in tmp_2:
                    tmp_board[i][idx] = n
                    idx += 1

    else:  # 상측으로 움직일 때
        for j in range(N):
            idx = 0
            tmp = deque()
            for i in range(N):
                if board[i][j] != 0:
                    tmp.append(board[i][j])

            if len(tmp) == 0:
                continue
            elif len(tmp) == 1:
                num = tmp.pop()
                tmp_board[idx][j] = num
            else:
                tmp_2 = []
                while tmp:
                    if len(tmp) == 1:
                        num = tmp.pop()
                        tmp_2.append(num)
                        break

                    if tmp[0] != tmp[1]:
                        num = tmp.popleft()
                        tmp_2.append(num)

                    elif tmp[0] == tmp[1]:
                        num = tmp.popleft()
                        tmp_2.append(num * 2)
                        tmp.popleft()

                for n in tmp_2:
                    tmp_board[idx][j] = n
                    idx += 1

    board = tmp_board
    t_board = sum(board, [])
    t_maxi = max(t_board)
    return board, t_maxi


def make_combs(cnt, board, tmp_maxi):
    global maxi

    if tmp_maxi < maxi // (2 ** (5 - cnt)):
        return

    if cnt == 5:
        ttmp = sum(board, [])
        t_num = max(ttmp)
        maxi = max(t_num, maxi)
        return

    copied_arr = [lst[:] for lst in board]

    for i in range(1, 5):
        calcul_arr, tmp_maxi = simulate(copied_arr, i)
        make_combs(cnt+1, calcul_arr, tmp_maxi)


N = int(input())
real_board = [list(map(int, input().split())) for _ in range(N)]
dir = [1, 2, 3, 4]  # 상우하좌 순서
maxi = 0
make_combs(0, real_board, 0)
print(maxi)