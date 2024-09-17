from collections import deque

def oob(i, j):
    return 0<=i<R and 0<=j<C

R, C = map(int, input().split())
room = [[0]*C for _ in range(R)]
k = int(input())
for _ in range(k):
    br, bc = map(int, input().split())
    room[br][bc] = -1

si, sj = map(int, input().split())
dir = {0:(-1, 0), 1:(1, 0), 2:(0, -1), 3:(0, 1)}
commands = list(map(lambda x:int(x)-1, input().split()))
room[si][sj] = 1

idx = 0
while True:
    flag = False

    for _ in range(4):
        command = commands[idx%4]

        di, dj = dir[command]
        ni, nj = si+di, sj+dj

        if oob(ni, nj) and room[ni][nj] == 0:
            room[ni][nj] = 1
            cnt = 0
            si, sj = ni, nj
            flag = True

        else:
            idx += 1

    if not flag:
        break

print(si, sj)