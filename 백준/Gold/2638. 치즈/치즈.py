'''
4변 중 2변 이상이 공기와 접촉 -> 한시간 만에 녹아서 없어짐
근데 치즈 내부에 난 구멍의 경우에는 공기와 접촉하지 않는 것으로 간주함
-> 그냥 빈공간 갯수로 체크하면 치즈 내부까지 체크가 되니까,
    같은 모양의 배열 하나 더 가지고 치즈 내부를 찾아서 미리 처리해줘야 할 듯
    모눈종이 맨 가장자리는 치즈 안 놓이니까 거기 기준으로 공기인 부분 처리하고
    다 처리했는데도 0인 부분이 있다면 거기는 내부인 것 ㅇㅇ
    공기 1 치즈 2 0인 부분은 그저 치즈 구멍
'''
from collections import deque

def noob(i, j):
    return 0<=i<N and 0<=j<M

def melt():
    global board

    tmp = [lst[:] for lst in board]
    for i in range(N):
        for j in range(M):
            if board[i][j] == 0: continue
            cnt = 0
            for di, dj in DIR:
                ni, nj = i+di, j+dj
                if not noob(ni, nj): continue
                if check[ni][nj] != 1: continue
                cnt += 1
            if cnt >= 2:  # 공기와 닿은 면이 두 개 이상일 때
                tmp[i][j] -= 1
                if tmp[i][j] < 0:
                    tmp[i][j] = 0

    board = tmp
    return


def check_bfs(si, sj):
    q = deque()
    visited = [[False for _ in range(M)] for _ in range(N)]
    visited[si][sj] = True
    check[0][0] = 1
    q.append((si, sj))

    while q:
        ci, cj = q.popleft()
        for di, dj in DIR:
            ni, nj = ci+di, cj+dj
            if noob(ni, nj) and not visited[ni][nj] and board[ni][nj] == 0:
                visited[ni][nj] = True
                check[ni][nj] = 1
                q.append((ni, nj))


N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
DIR = [(-1, 0), (0, 1), (1, 0), (0, -1)]

time = 0
while 1:
    # 바깥인 부분을 체크해 줄 bfs
    check = [[0 for _ in range(M)] for _ in range(N)]
    check_bfs(0, 0)
    melt()
    time += 1
    if sum(sum(board, [])) == 0:
        break
print(time)