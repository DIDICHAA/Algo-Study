from collections import deque

def simulate(board, d):
    # d 방향으로 board 밀고 그 결과 반환하는 함수
    tmp_board = [[0] * N for _ in range(N)]

    # 들어오는 d에 따라서 board 시계 방향으로 회전하면 되는 거 아닌감?
    # 기준은 오른쪽으로 잡고, 2, 3, 4가 들어왔을 때의 board 형태를 바꿔준다면

    if d == 2 or d == 3:
        board = list(map(list, zip(*board[::-1])))
        if d == 3:
            board = list(map(list, zip(*board[::-1])))
    if d == 4:
        board = list(map(list, zip(*board)))[::-1]

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

    board = tmp_board
    return board


def make_combs(cnt, board):
    global maxi

    ttmp = sum(board, [])
    t_num = max(ttmp)

    if t_num < maxi // (2 ** (5 - cnt)):
        return

    if cnt == 5:
        maxi = max(t_num, maxi)
        return

    for i in range(1, 5):
        calcul_arr = simulate(board, i)
        make_combs(cnt+1, calcul_arr)


N = int(input())
real_board = [list(map(int, input().split())) for _ in range(N)]
dir = [1, 2, 3, 4]  # 상우하좌 순서
maxi = 0
make_combs(0, real_board)
print(maxi)