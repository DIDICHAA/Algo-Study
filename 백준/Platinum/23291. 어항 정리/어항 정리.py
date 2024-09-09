'''
1449 문제 이해)
1. 물고기가 가장 적은 어항 += 물고기 1
    여러 개여도 똑같이 += 1
2. 가장 왼쪽의 어항을 그 오른쪽 어항 위에 올림
3. 2개 이상 쌓여있는 어항을 모두 오른쪽으로 90도 돌린 뒤
   -> 바닥에 놓인 가장 왼쪽과 어항의 가장 왼쪽이 맞닿게 올려줌 (반복)
    3-1. 들어올리고자 하는 어항의 len이 바닥에 놓인 어항의 len보다 길면 안 됨
        -> return, 물고기 수 조절하러 가야 함
4. 인접한 두 어항에 대해, 물고기 수의 차이를 구함
    - 이 차이를 //5 한 값이 d
        - d > 0 이라면 두 어항 중 물고기의 수가 많은 곳에 있는 d마리를
          물고기가 적은 어항으로 보냄
          (이 과정은 동시다발적으로 발생함)
          => (x, y, num)을 리스트에 저장한 뒤 모아놨다가 한 번에 해줘야 함
5. 다시 어항을 일렬로 펼침
    -> 열마다 가장 아래에 있는 어항이 가장 왼쪽에 오도록
6. 가운데를 중심으로 왼쪽 N//2개를 공중부양
    -> 전체를 시계 방향으로 180도 회전, 오른쪽 N//2개의 위에 위치
     => 두 번 반복
7. 4번에서 한 물고기 수 조절 작업 실시
8. 5번에서 한 바닥에 일렬로 펼치는 작업
// 여기까지 다 한 게 어항정리 한 번 한 거임 ㅁㅊ 돌았나 진짜

1500 구상
일단 넘버대로 함수로 구현하되, 시퀀스가 동일하므로 메인의 while문 안에서 실행
4 - 7, 5 - 8 번은 같은 함수 사용 // 헷갈리지 말고 호출
while문 종료조건은 함수를 8번까지 다 돌았을 때, max 어항 min 어항의 차이가 K이하가
되자마자 while문 종료하고 올려뒀던 cnt 출력

구현 포인트)
돌린 어항들을 어떻게 1차원 배열 위에 차곡차곡 쌓아줄 것인가?
일정한 크기의 0으로 찬 2차원 리스트를 선언해주고 거기에다가 움직인 애들 넣고 비교
가로는 N길이가 최대, 세로는 N//2가 최대
돌린 배열을 새로 놓는 위치는 현재의 i, j보다 i-1, j+1인 위치의 위에 놓게 됨

1512 구현 시작)
fish 리스트를 2차원이 아닌 1차원으로 관리하면서 빼주고 더해주는 로직 !!

'''
def oob(i, j, N, M):
    return 0<=i<M and 0<=j<N


def add_fish():
    # 어항 속 물고기가 가장 적은 어항에 물고기를 += 1 해주는 함수
    tmp = sum(fish, [])
    mini = min(tmp)
    for i in range(len(fish)):
        for j in range(len(fish[i])):
            if mini == fish[i][j]:
                fish[i][j] += 1

    return

# # 어항들을 조금씩 묶어 시계방향 90도로 돌리면서 j+1 위치로 이동


def rotate_fish():
    while True:  # 더이상 돌아갈 수 없을 때까지 회전시켜줘야 함
        # 리스트에 하나씩 접근해서 (for문)

        lst = []
        L = len(fish) - 1
        p = 0
        for i in range(L):
            if len(fish[i]) >= 2:
                now = fish[i]
                p += 1
                for j in range(len(now)):
                    lst.append((i, j, now[j]))

        for _ in range(p):
            fish.pop(0)

        lst.sort(reverse=True)
        for i in range(len(lst)):
            _, idx, n = lst[i]
            fish[idx].append(n)

        if (len(fish[0]) == len(fish) - 1) or (len(fish[0]) > len(fish[p:])):
            return

def cal_fish():
    N = len(fish[0])
    M = len(fish)
    # 이 함수 안에서 기존의 fish 배열을 2차원 배열안에 전부 넣은 뒤에 비교하면 안 될까?
    tmp_fish = [[-1]*N for _ in range(M)]  # -1로 찬 배열 먼저 선언

    # for문 돌면서 tmp_fish에다가 채워줌
    for i in range(M):
        for j in range(len(fish[i])):
            tmp_fish[i][j] = fish[i][j]

    add_lst = []
    # 사방 oob 검사해주면서 더 크면 //5를 d.. 어쩌고
    for i in range(M):
        for j in range(N):
            if tmp_fish[i][j] == -1: continue
            for di, dj in dir:
                ni, nj = i+di, j+dj
                if oob(ni, nj, N, M):
                    if tmp_fish[i][j] > tmp_fish[ni][nj] and tmp_fish[ni][nj] != -1:
                        value = tmp_fish[i][j] - tmp_fish[ni][nj]
                        d = value // 5
                        if d > 0:
                            add_lst.append((i, j, ni, nj, d))

    # 차이나는 애들을 다 메워줌
    for i, j, ni, nj, v in add_lst:
        tmp_fish[i][j] -= v
        tmp_fish[ni][nj] += v

    # 임의로 채워줬던 0은 전부 없애주기 ~
    for i in range(M):
        for j in range(N):
            if tmp_fish[i][j] != -1:
                fish[i][j] = tmp_fish[i][j]

    return

# 일렬로 펴주는 함수
def fish_jjuk():
    tmp = []
    for i in range(len(fish)):
        for j in range(len(fish[i])):
            tmp.append(fish[i][j])

    return tmp


# 가운데를 중심으로 왼쪽 N//2개를 공중 부양 시켜서 전체를 sort reverse 해준 뒤,
# pop 해주고 각 인덱스에 맞게 남은 fish에다가 append
# while len(fish)가 len(fish)//4가 될 때까지
def center_add_fish():
    cnt = 0

    while cnt != 2:
        cen = len(fish)//2
        tmp = []
        n = len(fish)//2 - 1
        step = 0
        for i in range(cen):
            for j in range(len(fish[i])-1, -1, -1):
                tmp.append((n, fish[i][j]))
            n -= 1
            step += 1

        # fish 배열에 넣어줌
        for _ in range(step):
            fish.pop(0)

        # tmp.sort(reverse=True)
        for idx, num in tmp:
             fish[idx].append(num)

        cnt += 1

    return


N, K = map(int, input().split())
# 각각의 숫자를 리스트로 쪼개서 마치 2차원 리스트인 것처럼 관리해야 함
# 1차원 리스트 받아서 2차원 리스트처럼 관리 못하남
tmp = list(map(int, input().split()))
fish = [n for n in map(list, zip(tmp))]
dir = [(0, 1), (0, -1), (1, 0), (-1, 0)]

ans = 0

while True:
    add_fish()
    # for a in fish:
    #     print(a)
    # print()
    # print('------최소 물고기 더하고--------')
    # 먼저 가장 왼쪽에 위치한 어항을 그 다음 위치의 위로 옮겨줌
    now = fish.pop(0)
    fish[0].append(*now)

    rotate_fish()  # ㅋㅋ 여기까지 2시간 걸림 실화가;
    # for a in fish:
    #     print(a)
    # print()
    # print('------어항 돌렸다리--------')

    cal_fish()
    # for a in fish:
    #     print(a)
    # print()
    # print('------인접 물고기 더했다리--------')

    ttmp = fish_jjuk()
    fish = [n for n in map(list, zip(ttmp))]
    # print(*fish)
    # print('------물고기 펼쳤다리--------')

    center_add_fish()
    # for a in fish:
    #     print(a)
    # print()
    # print('------ 중간에서 잘라서 붙여줬다리--------')

    cal_fish()
    # for a in fish:
    #     print(a)
    # print()
    # print('-----인접 물고기 또 더해줬다리--------')
    tttmp = fish_jjuk()
    fish = [n for n in map(list, zip(tttmp))]
    # print(*fish)
    # print('------물고기 또 펼쳐줬다리--------')

    ans += 1
    # print(ans, '번째였다리--------')

    res = sum(fish, [])
    maxi = max(res)
    mini = min(res)

    if(maxi - mini) <= K:
        break

print(ans)