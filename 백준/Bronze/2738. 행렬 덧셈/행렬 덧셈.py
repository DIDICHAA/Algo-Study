N, M= map(int, input().split())
board_A = [list(map(int, input().split())) for _ in range(N)]
board_B = [list(map(int, input().split())) for _ in range(N)]

for i in range(N):
    lst = []
    for j in range(M):
        lst.append(board_A[i][j]+board_B[i][j])
    print(*lst)