'''
문제 이해)
비비라기는 N*N인 격자에서 연습
격자의 각 칸에 위치한 바구니 (바구니는 좌표, A[r][c]는 바구니에 담긴 물의 양
(1,1) ~ (N,N)
1~N~1번 행과 열은 계속해서 이어짐

(N, 1), (N, 2), (N-1, 1), (N-1, 2) 네 군데에 비구름이 생김
비구름에게 M번의 이동 명령 // 이동 명령은 방향인 d와 거리인 s
방향은 총 8방

(이동 명령 시)
1. 모든 구름이 d 방향으로 s칸 이동
2. 각 구름에서 비가 내려 바구니에 저장된 물 += 1
3. 구름 모두 사라짐
4. 2번에서 물이 증가한 칸에 물복사 버그 사용,
    -> 대각선 방향으로 거리가 1인 칸에 물이 있는 바구니 수만큼 물 양 증가
    ## 이 때의 대각선은 경계 안에 있어야 함(계속해서 행/열이 이어지지 X)
5. 바구니에 저장된 물의 양이 2이상인 모든 칸에 구름 생성, 물 양 -= 2
    -> 이 때 구름이 생긴 칸 != 3번에서 구름이 사라진 칸
M 번의 이동이 모두 끝난 후 바구니에 들어있는 물의 양의 합

1439~
구상)
차례대로 구현하되, dir로 주어질 수 있는 방향이 8방인 점과
물복사 버그 사용시 대각선은 경계 안임을 체크해야 함
그 외에는 체크 없이 행/열이 계속해서 1~N~1로 이어질 수 있도록
i > N 일 경우, i = N - i 이런 식으로 초기화 하면 될 듯

1~2번 구름 이동 함수
-> 물이 증가한 칸일 때 물복사 버그 함수로 이동 // 이하 내용 수행
빠져나왔을 때 구름 없앰
4번 물복사 함수
-> 이하 내용 수행, oob 체크

M번의 이동을 다 수행할 때까지 전체를 감싸는 while문 필요
-> for문으로 대체

1444~
구현)

1545~
디버깅)
문제 1. grid에서 물이 올라가는 로직이 이상함.
제대로 안 올라가고 어디서 물이 새는 거 같음 ;;
86번 라인에서 range error가 뜨는데 이유를 모름
-> ni, nj가 엄청나게 작아지거나 커버려도 한 번만 더하거나 빼고 끝내서
range 처리가 제대로 안 됐음

문제2.
물의 양이 2 이상일 때 빼주는 걸 매 함수 돌릴 때마다 해줘서
물이 남아나질 않았음
-> 해당 for문 바깥으로 빼줌

문제3.
두 번째 이동에서부터 grid 안의 값이 이상하게 남기 시작

'''
def water_copy(lst):
    dir_2 = [(-1, 1), (1, 1), (1, -1), (-1, -1)]  # 거리가 1인 대각선 방향
    temp = []
    lst.sort()
    for i, j in lst:
        cnt = 0
        for di, dj in dir_2:
            ni, nj = i+di, j+dj  # 물의 양을 체크할 대각선 방향

            if 0<=ni<N and 0<=nj<N and grid[ni][nj] != 0:  # 대각선은 경계를 넘어서면 안 됨
                cnt += 1  # 대각선에 있는 물이 있는 바구니 수 만큼 증가
        grid[i][j] += cnt


def move_cloud(d, s):
    # 초기 구름이 생긴 방향으로부터 d 방향으로 s칸 이동
    di, dj = dir[d-1]  # d의 방향에 해당하는 값
    ni, nj = di*s, dj*s  # s 거리만큼 이동
    lst = []

    for i in range(N):
        for j in range(N):
            if cloud[i][j] == 1:
                tn = i+ni
                tm = j+nj
                while tn < 0:
                    tn += N
                while tn >= N:
                    tn -= N
                while tm < 0:
                    tm += N
                while tm >= N:
                    tm -= N

                lst.append((tn, tm))
                cloud[i][j] = 0  # 기존 비구름 위치에서 구름 없앰

    for i, j in lst:
        cloud[i][j] = 1  # 모아뒀다가 한 번에 구름 생기게 함
        grid[i][j] += 1  # 물의 양이 1 증가하고
        # cloud[i][j] = 0  # 비구름은 사라진다

    water_copy(lst)  # 물이 증가한 칸에 물복사 버그 시전

    for x in range(N):
        for y in range(N):
            if grid[x][y] >= 2 and cloud[x][y] == 0:
                cloud[x][y] = 1  # 물의 양이 2 이상이면 구름 생김
                grid[x][y] -= 2  # 그리고 물은 2 사라짐

    for i, j in lst:
        cloud[i][j] = 0


N, M = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(N)]
cloud = [[0]*N for _ in range(N)] # 구름을 체크할 배열

dir = [(0, -1), (-1, -1), (-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1)]  # 8방 탐색
cloud[N-1][0], cloud[N-1][1], cloud[N-2][0], cloud[N-2][1] = 1, 1, 1, 1

for _ in range(M):
    d, s = map(int, input().split())
    move_cloud(d, s)

sm = 0
for lst in grid:
    for n in lst:
        sm += n
print(sm)