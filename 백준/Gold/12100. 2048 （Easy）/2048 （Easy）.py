'''
2048 문제 이해)
어떻게 문제 풀기 시작한 시간도 2048

같은 값을 갖는 두 블록이 충돌 -> 하나로 합쳐짐
한 번의 이동에서 이미 합쳐진 블록은 다른 블록과 합쳐질 수 없음
보드 크기와 보드판의 상태가 주어졌을 때 최다 5번 이동해서 만들 수 있는 가장 큰 블록의 값

2050 구상
일단 상하좌우 기준으로 만들 수 있는 5번의 움직임 - 중복순열을 만들고,
만들어질 때마다 함수로 넘어가서 해당 방향에 맞춰 움직일 수 있도록 해야 함
같은 사이즈의 배열 하나 더 만들어서 idx값 비교하면서 넣는 중력

2051 구현
'''
from collections import deque
def move_board(lst, board):
    for n in lst:
        tmp_board = [[0] * N for _ in range(N)]

        if n == 1:  # 우측으로 움직일 떄
            for i in range(N):
                idx = N-1
                tmp = deque()
                for j in range(N-1, -1, -1):
                    if board[i][j] != 0:
                        tmp.append(board[i][j])

                if len(tmp) == 0: continue
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
                            tmp_2.append(num*2)
                            tmp.popleft()  # 같은 숫자 두 개니까 한 번 더 빼줌..

                    for n in tmp_2:
                        tmp_board[i][idx] = n
                        idx -= 1

        elif n == 2:  # 하측으로 움직일 떄
            for j in range(N):
                idx = N-1
                tmp = deque()
                for i in range(N-1, -1, -1):
                    if board[i][j] != 0:
                        tmp.append(board[i][j])

                if len(tmp) == 0: continue
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
                            tmp_2.append(num*2)
                            tmp.popleft()

                    for n in tmp_2:
                        tmp_board[idx][j] = n
                        idx -= 1

        elif n == 3:  # 좌측으로 움직일 떄
            for i in range(N):
                idx = 0
                tmp = deque()
                for j in range(N):
                    if board[i][j] != 0:
                        tmp.append(board[i][j])

                if len(tmp) == 0: continue
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
                            tmp_2.append(num*2)
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

                if len(tmp) == 0: continue
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
                            tmp_2.append(num*2)
                            tmp.popleft()

                    for n in tmp_2:
                        tmp_board[idx][j] = n
                        idx += 1

        board = tmp_board
    return board


def make_combs(cnt, lst, board):
    global maxi

    if cnt == 5:
        res_board = move_board(lst, board)
        # print(*res_board, sep='\n')
        # print('########### 구분선 #############')
        ttmp = sum(res_board, [])
        t_num = max(ttmp)
        maxi = max(t_num, maxi)
        return

    for i in range(len(dir)):
        lst.append(dir[i])
        make_combs(cnt+1, lst, board)
        lst.pop()


N = int(input())
real_board = [list(map(int, input().split())) for _ in range(N)]
dir = [1, 2, 3, 4]  # 상우하좌 순서
maxi = 0
make_combs(0, [], real_board)
print(maxi)