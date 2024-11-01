from collections import deque

def noob(i, j):
    return 0<=i<N and 0<=j<2*N

def calcul(arr, num, tile):
    lst = [tile, num]
    while 1:
        if num == 1:
            break
        for i in range(N):
            for j in range(2*N):
                if nums[i][j] == num:
                    num = arr[i][j]
                    lst.append(num)
    lst = lst[::-1]
    return lst

def bfs():
    q = deque()
    visited = [[0 for _ in range(2*N)] for _ in range(N)]
    q.append((0, 0))
    q.append((0, 1))
    visited[0][0], visited[0][1] = 1, 1

    while q:
        ci, cj = q.popleft()
        if nums[ci][cj] == max_num:
            return visited, visited[ci][cj], max_num

        for di, dj in DIR:
            ni, nj = ci+di, cj+dj
            if not noob(ni, nj): continue
            if visited[ni][nj]: continue
            if board[ci][cj] == board[ni][nj]:
                visited[ni][nj] = nums[ci][cj]
                q.append((ni, nj))
                for ddi, ddj in ((0, 1), (0, -1)):
                    nni, nnj = ni+ddi, nj+ddj
                    if noob(nni, nnj) and not visited[nni][nnj] and nums[nni][nnj] == nums[ni][nj]:
                        visited[nni][nnj] = visited[ni][nj]
                        q.append((nni, nnj))

    for i in range(N-1, -1, -1):
        for j in range(2*N-1, -1, -1):
            if not visited[i][j]: continue
            return visited, visited[i][j], nums[i][j]


N = int(input())
board = [[0 for _ in range(2*N)] for _ in range(N)]
nums = [[0 for _ in range(2*N)] for _ in range(N)]
DIR = [(-1, 0), (0, 1), (1, 0), (0, -1)]

num = 1
for i in range(N):
    if i%2 != 0:  # 홀수 줄일 때
        idx = 1
        for _ in range(N-1):
            x, y = map(int, input().split())
            board[i][idx], board[i][idx+1] = x, y
            nums[i][idx], nums[i][idx+1] = num, num
            idx += 2
            num += 1

    elif i%2 == 0:  # 짝수 줄일 때
        idx = 0
        for _ in range(N):
            x, y = map(int, input().split())
            board[i][idx], board[i][idx+1] = x, y
            nums[i][idx], nums[i][idx+1] = num, num
            idx += 2
            num += 1

max_num = max(sum(nums, []))
arr, last_num, last_tile = bfs()
lst = calcul(arr, last_num, last_tile)
print(len(lst))
print(*lst)