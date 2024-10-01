'''
1. 문제 한 번 가볍게 정독하기 - yes!
2. 문제 한 번 더 읽으면서 주석에 주요 내용 정리하기 - yes!
3. 입력 받고 확인하기
4. 메인 짜고 흐름이 맞는지 문제 지문과 비교하며 확인하기
4-1. 메인에서 while문을 썼다면, 종료 조건이 제대로 작동하는지 확인하기
5. 함수 짤 때마다(혹은 연결된 함수 단위로) 배열 전부 까서 확인하기
6. queue나 list의 자료구조가 빌 때 예외처리를 해줬는 지 확인하기
7. 테스트 케이스 실행 시켜서 답 확인하기 전,
    모든 함수가 문제에서 요구하는 대로 흘러가고 있는지
    * 꼼꼼히, 하나씩 확인하기 *
8. 디버깅 시, 무작정 디버거만 돌리지 않고, 라인 별로 의미 생각하며 보기
8-1. 구현 시 애매하다고 생각한 부분은 북마크 해두기

각 cctv 넘버마다 가능한 방향 조합 DIR 선언
dfs로 이 조합 DIR의 인덱스 넘버 조합을 만든다고 생각해보자
그럼 완탐해서 지금 방 안에 있는 cctv_lst를 만들고, 얘네 넘버에 맞게
각자의 DIR 안에서 방향 모음을 가리키는... 인덱스 조합을 만들어서
calcul로 보내줌 (cnt == len(cctv_lst))가 됐을 때 - max값 갱신
어차피 cctv_lst는 전역으로 쓰면서 calcul안에서 비교대조 하면서 돌려주면 됨
'''
def noob(i, j):
    return 0<=i<N and 0<=j<M


def calcul(lst):
    global total

    tmp_arr = [row[:] for row in room]
    cnt = 0
    if N > M:
        mm = N
    else:
        mm = M

    for i in range(len(cctv_lst)):
        direction = lst[i]
        cctv = cctv_lst[i]
        x, y = grid_lst[i]
        if len(direction) > 1:  # 2개 이상의 방향으로 뻗어나가야 할 때
            for d in direction:
                di, dj = DIR[d]
                for mul in range(1, mm):
                    ni, nj = x+di*mul, y+dj*mul
                    if noob(ni, nj) and room[ni][nj] == 6:
                        break
                    if noob(ni, nj) and room[ni][nj] == 0:
                        tmp_arr[ni][nj] = '#'
        else:
            di, dj = DIR[direction[0]]
            for mul in range(1, mm):
                ni, nj = x+di*mul, y+dj*mul
                if noob(ni, nj) and room[ni][nj] == 6:
                    break
                if noob(ni, nj) and room[ni][nj] == 0:
                    tmp_arr[ni][nj] = '#'

    tmp = sum(tmp_arr, [])
    cnt = tmp.count(0)
    total = min(total, cnt)
    return



def make_comb(cnt, idx, lst):
    if cnt == len(cctv_lst):
        calcul(lst)
        return

    for i in range(idx, len(cctv_lst)):
        num = cctv_lst[i]
        direction = DICT[num]
        for n in range(len(direction)):
            dirr = direction[n]
            lst.append(dirr)
            make_comb(cnt+1, i+1, lst)
            lst.pop()




N, M = map(int, input().split())
room = [list(map(int, input().split())) for _ in range(N)]
DIR = [(-1, 0), (0, 1), (1, 0), (0, -1)]  # 기본 DIR
# 각 cctv 넘버마다 뻗어나갈 수 있는 방향을 DIR 기준으로 인덱스 값을 넣어서 만들어줌
DIR_1 = [[0], [1], [2], [3]]
DIR_2 = [[0, 2], [1, 3]]
DIR_3 = [[0, 1], [1, 2], [2, 3], [3, 0]]
DIR_4 = [[0, 1, 3], [1, 2, 3], [2, 3, 0], [0, 1, 2]]
DIR_5 = [[0, 1, 2, 3]]
total = 1e9  # 최종적으로 출력할 변수
DICT = {1:DIR_1, 2:DIR_2, 3:DIR_3, 4:DIR_4, 5:DIR_5}
cctv_lst = []
grid_lst = []
for i in range(N):
    for j in range(M):
        if room[i][j] != 0 and room[i][j] != 6:
            cctv_lst.append(room[i][j])  # 방에 위치한 cctv 값을 전부 넣어줌
            grid_lst.append((i, j))

make_comb(0, 0, [])
print(total)