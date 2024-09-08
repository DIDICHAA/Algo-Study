'''
새로 세울 수 있는 벽의 개수는 3개, 이 3개를 반드시 세워야 함
-> 백트래킹으로 가능한 좌표의 조합 3개 만들어서 1 넣고 bfs 돌려서 max safe 구하기
    -> 우선 좌표가 0인 애들 중에서 1을 세울 수 있는 좌표를 전부 넣고, 이 좌표 중 백트래킹으로 조합 만들기
'''
from collections import deque
import copy

def oob(i, j):
    return 0<=i<N and 0<=j<M

def check_safe(visited, lab_copy):
    global ans
    q = deque()

    for i in range(N):
        for j in range(M):
            if lab_copy[i][j] == 2:
                q.append((i, j))
                visited[i][j] = 1
            if lab_copy[i][j] == 1:
                visited[i][j] = 1

    while q:
        ci, cj = q.popleft()
        for di, dj in dir:
            ni, nj = ci+di, cj+dj
            if oob(ni, nj) and lab_copy[ni][nj] != 1 and visited[ni][nj] == 0:
                visited[ni][nj] = 1
                q.append((ni, nj))


    tmp = sum(visited, [])
    tp_ans = tmp.count(0)
    ans = max(ans, tp_ans)
    return


def make_comb(cnt, idx, lst):
    if cnt == 3:
        lab_copy = copy.deepcopy(lab)
        for x, y in lst:
            lab_copy[x][y] = 1

        visited = [[0] * M for _ in range(N)]
        check_safe(visited, lab_copy)
        return

    for i in range(idx, len(none_lst)):
        lst.append(none_lst[i])
        make_comb(cnt+1, i+1, lst)
        lst.pop()


N, M = map(int, input().split())
lab = [list(map(int, input().split())) for _ in range(N)]
none_lst = []
ans = 0
dir = [(0, 1), (0, -1), (1, 0), (-1, 0)]
for i in range(N):
    for j in range(M):
        if lab[i][j] == 0:
            none_lst.append((i, j))

make_comb(0, 0, [])
print(ans)