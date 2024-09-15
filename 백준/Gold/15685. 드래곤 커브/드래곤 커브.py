'''
** 2시간 잡고 풀어보기 **
** 기존의 아이디어에 갇히지 말고 풀어보자 **

문제에서 주어진 x, y 좌표는 일반적으로 쓰는 i, j 좌표를 반대로 해둔 것
덱에 마지막으로 들어가있느 선분부터 차례대로 빼내면서

각 세대의 끝점에서 (-1, 0)을 더한 게 그 다음 세대의 첫 점

새로 생기는 직선이 문제에서 제시한 dir 안에서 움직이는데 세대에 따라서 다르니까..
그거 규칙성 가지고 curve list를 먼저 만들어주기

네 꼭짓점 세는 건 2*2 스퀘어가 겹쳐도 ㄱㅊ으니 몇 개냐 == 꼭짓점이 다 드래곤 커브인 1*1 정사각형이 됨

'''
def make_curves(tj, ti, d, g):
    grid[ti][tj] = 1

    curve = [d]
    for i in range(g):
        for j in range(len(curve)-1, -1, -1):
            curve.append((curve[j]+1)%4)

    for i in range(len(curve)):
        di, dj = dir[curve[i]]
        ni, nj = ti+di, tj+dj
        grid[ni][nj] = 1
        ti, tj = ni, nj


N = int(input())
dir = [(0, 1), (-1, 0), (0, -1), (1, 0)]  # 문제에서 요구한 우상좌하 순서

grid = [[0]*102 for _ in range(102)]  # 드래곤 커브를 1로 채워줄 grid 선언

for _ in range(N):
    sj, si, d, gen = map(int, input().split())
    make_curves(sj, si, d, gen)  # 매 드래곤 커브마다 함수 돌면서 그리드에 표시

total = 0
for i in range(102):
    for j in range(102):
        if grid[i][j] == 1 and grid[i][j+1] == 1 and grid[i+1][j] == 1 and grid[i+1][j+1] == 1:
            total += 1

print(total)