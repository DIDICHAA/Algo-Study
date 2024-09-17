'''
1926 진짜 찐막 경사로 풀기 시작
행 하나씩, 그리고 현재 위치의 인덱스에서 하나씩 검사
'''
# def check_ground(x, j, k, jido):
#     # 모든 체크 함수는 j부터 j+L까지의 범위만 확인하면 됨 당장의 이 칸들이
#     # 경사로가 놓아질 수 있는 길인지, 평지가 가능한 길인지
#     flag = True
#     for y in range(j, k):
#         if jido[x][y] != jido[x][y+1]:
#             flag = False
#
#     if flag:
#         return True
#     else:
#         return False


def check_upper(x, j, k, jido):
    # 딱 들어온 구간에 대해서만 L길이의 상향 경사로가 놓일 수 있는 지 확인하기
    cnt = 0
    if j-L+1 < 0:
        return False
    if L == 1:
        if used[j]:
            return False

    sset = set()
    sset.add(j)
    for y in range(j, j-L+1, -1):
        if y > 0 and jido[x][y] == jido[x][y-1] and not used[y-1]:
            cnt += 1
            sset.add(y)
            sset.add(y-1)
    if cnt == L-1:
        for n in sset:
            used[n] = True
        return True
    else:
        return False


def check_lower(x, j, k, jido):
    cnt = 0

    sset = set()
    sset.add(j+1)
    for y in range(j+1, k):
        if y+1 < N and jido[x][y] == jido[x][y+1]:
            sset.add(y)
            sset.add(y+1)
            cnt += 1

    if cnt == L-1:
        for n in sset:
            used[n] = True
        return True
    else:
        return False


N, L = map(int, input().split())
jido = [list(map(int, input().split())) for _ in range(N)]

total = 0
for i in range(N):
    used = [False]*N
    j = 0
    flag = False

    while j < N-1:

        if jido[i][j] == jido[i][j+1]:
            j += 1
        elif jido[i][j] + 1 == jido[i][j+1]:
            flag = check_upper(i, j, j+L, jido)
            if flag:
                j += 1
            else:
                break
        elif jido[i][j] == jido[i][j+1] + 1:
            flag = check_lower(i, j, j+L, jido)
            if flag:
                j = j+L
            else:
                break
        else:
            break
    if j == N-1:
        total += 1


jido_rotate = list(map(list, zip(*jido)))
for i in range(N):
    used = [False] * N
    j = 0
    flag = False

    while j < N-1:
        if jido_rotate[i][j] == jido_rotate[i][j+1]:
            j += 1
        elif jido_rotate[i][j] + 1 == jido_rotate[i][j+1]:
            flag = check_upper(i, j, j+L, jido_rotate)
            if flag:
                j += 1
            else:
                break
        elif jido_rotate[i][j] == jido_rotate[i][j+1] + 1:
            flag = check_lower(i, j, j+L, jido_rotate)
            if flag:
                j = j+L
            else:
                break
        else:
            break
    if j == N-1:
        total += 1

print(total)