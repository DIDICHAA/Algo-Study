from collections import deque

def iob(l, i, j):
    return  0<=l<5 and 0<=i<5 and 0<=j<5


def make_rot_comb(cnt, lst):
    if cnt == 5:
        n_lst = lst[:]
        rotate_lsts.append(n_lst)
        return

    for i in range(4):
        lst.append(i)
        make_rot_comb(cnt+1, lst)
        lst.pop()


def make_ord_comb(cnt, lst):
    if cnt == 5:
        n_lst = lst[:]
        ord_lsts.append(n_lst)
        return

    for i in range(5):
        if not v_ord[i]:
            v_ord[i] = True
            lst.append(i)
            make_ord_comb(cnt+1, lst)
            lst.pop()
            v_ord[i] = False


def make_cube(rotate_lst, ord_lst):
    tmp = []

    for n in range(5):
        arr = arr_dict[ord_lst[n]]
        if rotate_lst[n] == 0:
            tmp += [arr]
        elif rotate_lst[n] == 1:
            arr = [list(map(list, zip(*arr[::-1])))]
            tmp += arr
        elif rotate_lst[n] == 2:
            arr = list(map(list, zip(*arr[::-1])))
            arr = [list(map(list, zip(*arr[::-1])))]
            tmp += arr
        else:
            arr = [list(map(list, zip(*arr)))[::-1]]
            tmp += arr

    return tmp


def bfs(arr):
    global ans

    q = deque()
    visited = [[[0 for _ in range(5)] for _ in range(5)] for _ in range(5)]
    si, sj, sl = 0, 0, 0

    q.append((sl, si, sj))
    visited[sl][si][sj] = 1

    while q:
        cl, ci, cj = q.popleft()
        if (ci, cj, cl) == (4, 4, 4):
            ans = min(ans, visited[cl][ci][cj]-1)
            return

        for dl, di, dj in DIR:
            nl, ni, nj = cl+dl, ci+di, cj+dj
            if not iob(nl, ni, nj): continue
            if visited[nl][ni][nj] != 0: continue
            if arr[nl][ni][nj] == 0: continue
            q.append((nl, ni, nj))
            visited[nl][ni][nj] = visited[cl][ci][cj] + 1


arr1 = [list(map(int, input().split())) for _ in range(5)]
arr2 = [list(map(int, input().split())) for _ in range(5)]
arr3 = [list(map(int, input().split())) for _ in range(5)]
arr4 = [list(map(int, input().split())) for _ in range(5)]
arr5 = [list(map(int, input().split())) for _ in range(5)]

ans = 1e9

DIR = [(-1, 0, 0), (1, 0, 0), (0, -1, 0), (0, 0, 1), (0, 1, 0), (0, 0, -1)]

# 회전을 몇 번 할 건지에 대한 조합
rotate_lsts = []
make_rot_comb(0, [])

v_ord = [False] * 5
ord_lsts = []
make_ord_comb(0, [])
tmp_arr = []

arr_dict = {0:arr1, 1:arr2, 2:arr3, 3:arr4, 4:arr5}
# 어떤 순서로 쌓을 건지에 대한 조합
for rotate_lst in rotate_lsts:
    for ord_lst in ord_lsts:
        new_arr = make_cube(rotate_lst, ord_lst)
        if tmp_arr == new_arr: continue
        else:
            tmp_arr = new_arr
        # 두 조합을 곱해서 나오는 모든 경우의 수마다 bfs
        if new_arr[0][0][0] == 0 or new_arr[4][4][4] == 0: continue
        bfs(new_arr)

if ans == 1e9:
    print(-1)
else:
    print(ans)