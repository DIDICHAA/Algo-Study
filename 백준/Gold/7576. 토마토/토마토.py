from collections import deque

# BFS를 활용해 하루 단위로 익음을 전파
def bfs():
    queue = deque()
    visited = [[0 for _ in range(cols)] for _ in range(rows)]
    for row in range(rows):
        for col in range(cols):
            if grid[row][col] == 1:  # 익은 토마토의 위치를 큐에 추가
                queue.append((row, col))
                visited[row][col] = 1

    while queue:
        row, col = queue.popleft()
        for i in range(4):
            nxt_row, nxt_col = row + drs[i], col + dcs[i]
            if not (0 <= nxt_row < rows and 0 <= nxt_col < cols): continue
            if grid[nxt_row][nxt_col] != 0: continue
            if visited[nxt_row][nxt_col] != 0: continue
            visited[nxt_row][nxt_col] = visited[row][col] + 1
            queue.append((nxt_row, nxt_col))

    # 익지 않은 토마토가 남아있는지 확인
    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == -1: continue
            if visited[i][j] != 0: continue
            return -1
    return max(sum(visited, []))-1

# 입력 처리
cols, rows = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(rows)]
drs = [0, 0, 1, -1]
dcs = [1, -1, 0, 0]

print(bfs())
