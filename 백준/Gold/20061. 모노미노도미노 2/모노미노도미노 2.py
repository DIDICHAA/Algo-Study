'''
1. 문제 한 번 가볍게 정독하기 - yes
2. 문제 한 번 더 읽으면서 주석에 주요 내용 정리하기 - yes 종이 설계함
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

블럭을 올려 놓으면 .. 파란색 배열은 오른쪽으로 중력이 작용하는 거고
초록색 배열은 아래로 중력이 작용하는 거임 각각 배열 따로 만들어서 관리하기
빨간색 배열까지 포함한 긴 어레이가 굳이 필요할까? 웅

1.파 array는 전치시키고, x y 값 calcul한 다음에 자리 바꿔서 블럭 넣고
그대로 중력으로 내려주기
2.초 array는 원래 그대로 x,y값 calcul 한 다음에 쭉 내려주기
// 이 때 블럭 하나 당 단위가 아니라, 2개 일 때는 그 갯수에 따라서
while문으로 아래에서 위부터 탐색하면서 j고정 / i 바뀌면서 그 두 자리가 0인 곳
찾아서 바로 넣어주기 (1로) 이거 넣어주면 break

while로 type에 따라 가능할 때까지 내려주고 // 변수 저장하면서 내려주고
아니면 바로 break해서 변수에는 이전 턴의 i, j 값이 저장될 수 있도록
break 됐을 때 기존 좌표값은 0으로 만들어주고 new 좌표값에다가 num 넣어주기
-> 이게 3번에 해당 (후술할 거임)

1. 블럭 별로 가능한 위치까지 내려주고 (3번 함수)
2. 두 개의 배열 행 검사해서 없애주고 / 점수 올려주고
3. 블럭 싹 내려주기 (얘가 그 3번 함수임)
4. 위의 라인 2개 검사
    -> 걸린 행 갯수만큼 [N-1][:] 없애줌 그리고 전체 끌어 내리기
-- 요 시퀀스를 각 블럭마다 반복해주면 됩니다잉
출력 : 얻은 점수 / 파+초 안 속 타일이 드가있는 칸 갯수

1. blue 배열에 x, y, 안 돌려서 넣었는데 이거 말고도 뭔가가 더 들어가는 이슈가 ..
2. zㅋㅋㅋ  배열 두 개 다 난리났노 ... whyrano.. whyrano ....

'''


def noob(i, j):
    return 0 <= i < 6 and 0 <= j < 4


def down_block(t, x, y, num, color):
    # t == 1일 때 먼저 처리, 초록/파랑 각각의 배열에서 동시 처리
    if t == 1:
        if color == 'green':
            gx, gy = x, y
            while 1:
                if gx < 5 and green[gx + 1][gy] == 0:
                    gx += 1
                else:
                    break
            green[gx][gy] = num  # green 배열에 먼저 넣어줘볼까
        elif color == 'blue':
            bx, by = x, y
            while 1:
                if bx < 5 and blue[bx + 1][by] == 0:
                    bx += 1
                else:
                    break
            blue[bx][by] = num

    elif t == 2:  # 가로 2개일 때
        if color == 'green':
            ngi, ngj = x, y
            while ngi < 6:
                if green[ngi][ngj] == 0 and green[ngi][ngj + 1] == 0:  # 행 하나씩 내리면서 연속 두 개가 가능한지
                    ngi += 1
                else:
                    break
            green[ngi - 1][ngj], green[ngi - 1][ngj + 1] = num, num

        elif color == 'blue':
            nbi, nbj = x, y
            while nbi < 6:
                if blue[nbi][nbj] == 0 and blue[nbi][nbj + 1] == 0:
                    nbi += 1
                else:
                    break
            blue[nbi-1][nbj], blue[nbi-1][nbj + 1] = num, num

    else:
        if color == 'green':
            ngi, ngj = 0, y
            while ngi < 5:
                if green[ngi + 1][ngj] == 0:  # 행 하나씩 내리면서 연속 두 개가 가능한지
                    ngi += 1
                else:
                    break
            green[ngi-1][ngj], green[ngi][ngj] = num, num

        elif color == 'blue':
            nbi, nbj = 0, y
            while nbi < 5:
                if blue[nbi + 1][nbj] == 0:
                    nbi += 1
                else:
                    break
            blue[nbi-1][nbj], blue[nbi][nbj] = num, num

    return


def check_array():
    global total
    '''
    2. 두 개의 배열 행 검사해서 없애주고 / 점수 올려주고 
    '''
    for i in range(6):
        g_flag = True
        b_flag = True
        for j in range(4):
            if green[i][j] == 0:
                g_flag = False
            if blue[i][j] == 0:
                b_flag = False

        if g_flag:
            green[i][:] = [0, 0, 0, 0]
            move_down(i, 'green')
            total += 1
        if b_flag:
            blue[i][:] = [0, 0, 0, 0]
            move_down(i, 'blue')
            total += 1
    return


def move_down(i, color):
    global green, blue
    '''
    이후에는 초록색 보드에서 사라진 행의 위에 있는 블록이 사라진 행의 수만큼 아래로 이동한다.
    '''
    tmp_arr = [[0 for _ in range(4)] for _ in range(6)]
    if color == 'green':
        # tmp_arr의 ~ i+1까지를 green의 ~i까지 값으로 넣어줘야 함 그리고 그 이후 값은 green..
        for x in range(i):
            for y in range(4):
                tmp_arr[x+1][y] = green[x][y]
        for x in range(i+1, 6):
            for y in range(4):
                tmp_arr[x][y] = green[x][y]
        green = tmp_arr

    elif color == 'blue':
        for x in range(i):
            for y in range(4):
                tmp_arr[x+1][y] = blue[x][y]
        for x in range(i+1, 6):
            for y in range(4):
                tmp_arr[x][y] = blue[x][y]
        blue = tmp_arr

    return


def check_upper():
    global green, blue
    # green
    g_flag = False
    g_cnt = 0
    g_tmp = [[0 for _ in range(4)] for _ in range(6)]
    for i in range(2):
        for j in range(4):
            if green[i][j] != 0:
                g_flag = True
                g_cnt += 1
                break
    if g_flag:
        g_tmp[g_cnt:] = green[:6 - g_cnt]
        green = g_tmp

    # blue
    b_flag = False
    b_cnt = 0
    b_tmp = [[0 for _ in range(4)] for _ in range(6)]
    for i in range(2):
        for j in range(4):
            if blue[i][j] != 0:
                b_flag = True
                b_cnt += 1
                break
    if b_flag:
        b_tmp[b_cnt:] = blue[:6 - b_cnt]
        blue = b_tmp

    return


N = int(input())
green = [[0 for _ in range(4)] for _ in range(6)]
blue = [[0 for _ in range(4)] for _ in range(6)]
DIR = [(-1, 0), (0, 1), (1, 0), (0, -1)]
block_2 = [[0, 0], [0, 1]]
block_3 = [[0, 0], [1, 0]]
block_dict = {2: block_2, 3: block_3}
total = 0  # 최종 출력 변수

for i in range(1, N + 1):
    t, x, y = map(int, input().split())
    down_block(t, 0, y, i, 'green')  # 초, 파 각각 해줘야 됨
    if t == 2:
        t = 3
    elif t == 3:
        t = 2
    down_block(t, 0, x, i, 'blue')  # 초, 파 각각 해줘야 됨
    check_array()
    check_upper()
    # print(*green, sep='\n')
    # print('##############################')
    # print(*blue, sep='\n')
    # print('##############################')

print(total)
gtmp = sum(green, [])
btmp = sum(blue, [])
print(48 - gtmp.count(0) - btmp.count(0))