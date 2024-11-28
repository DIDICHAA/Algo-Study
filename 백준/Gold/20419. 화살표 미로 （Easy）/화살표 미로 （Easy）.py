'''
주문서는 0개 or 1개 세트
1개 세트 : L + R 하나씩
K가 0이면 그냥 현재 상태에서 나올 수 있어야 되고,
K가 1이면 L하나, R하나까지 쓸 수 있음 그럼 visit 관리를
3차원으로 해서 [0, 0, 0, 0]
not used, left used, right used, both used 이런 식으로 ..
K범위가 늘어나는 Hard 같은 건 visited 안에서 누적합으로 넣어주고
K만큼 도달했냐를 확인해주는 로직을 넣으면 되지 않을까?

'''
from collections import deque


def iob(i, j):
    return 0<=i<R and 0<=j<C


def bfs(si, sj):
    q = deque()
    visited = [[[False for _ in range(4)] for _ in range(C)] for _ in range(R)]
    q.append((si, sj, 0))
    visited[si][sj][0] = True

    while q:
        ci, cj, status = q.popleft()
        if (ci, cj) == (R-1, C-1):
            return True

        d = DIR_DICT[board[ci][cj]]
        di, dj = DIR[d]
        ni, nj = ci+di, cj+dj

        # both have any or not
        if iob(ni, nj) and not visited[ni][nj][status]:
            q.append((ni, nj, status))
            visited[ni][nj][status] = True

        # if have any set
        if K > 0:
            if status == 3: continue

            # only one-side was used
            elif status == 2 or status == 1:
                if status == 2:  # right was used
                    d = (d-1)%4
                else:  # left was used
                    d = (d+1)%4

                ddi, ddj = DIR[d]
                nni, nnj = ci+ddi, cj+ddj
                if not iob(nni, nnj): continue
                if visited[nni][nnj][3]: continue
                visited[nni][nnj][3] = True
                q.append((nni, nnj, 3))

            # nothing was used
            else:
                ldi, ldj = DIR[(d-1)%4]
                rdi, rdj = DIR[(d+1)%4]
                lndi, lndj = ci+ldi, cj+ldj
                rndi, rndj = ci+rdi, cj+rdj

                if iob(lndi, lndj) and not visited[lndi][lndj][1]:
                    visited[lndi][lndj][1] = True
                    q.append((lndi, lndj, 1))

                if iob(rndi, rndj) and not visited[rndi][rndj][2]:
                    visited[rndi][rndj][2] = True
                    q.append((rndi, rndj, 2))

    return False


R, C, K = map(int, input().split())
board = [list(map(str, input())) for _ in range(R)]
DIR_DICT = {'U':0, 'R':1, 'D':2, 'L':3}
DIR = [(-1, 0), (0, 1), (1, 0), (0, -1)]

if bfs(0, 0):
    print('Yes')
else:
    print('No')