'''
** 맥시멈 2시간 잡고 문제 풀기 **
** 문제에서 요구하는 대로 구현하기 **
** 뇌피셜 금지 **
** 인덱스 유의하기 **

1857 문제 이해

1초가 지날 때마다 배열에 연산이 적용된다
R 연산 : 배열 A의 모든 행에 대해 정렬, 행 >= 열의 개수 일 때만
C 연산 : 배열 A의 모든 열에 대해 정렬, 행 < 열의 개수 일 때만

한 행 or 열에 있는 수를 정렬하려면 각각의 수가 몇 번 나왔는지 알아야 한다.
-> 수의 등장 횟수가 커지는 순으로, 그러한 것이 여러 개라면 수가 커지는 순으로 정렬
그 다음에는 배열 A에 정렬된 결과를 다시 넣어야 함.
[수, 등장 횟수] 순서로

예컨대 [3, 1, 1] 이라는 배열이 있다면 ... 정렬된 결과는 [3, 1, 1, 2]
1이 2번 2와 3이 각각 1번 나옴
2 1(번) 3 1(번) 1 (2번) 이 되기 때문에 배열 A는 [2 1 3 1 1 2] 가 된다
연산이 적용된 뒤에 크기가 변해서 남는 공간에는 0을 채워준다.
** 수 정렬 시 0은 무시!
행 또는 열의 크기가 100을 넘어가면, 처음 100개를 제외한 그 뒤의 것들은 버린다
A[r][c]의 값이 K가 되기 위해 걸리는 최소 시간은?

1904 구상)
쓰읍... while문 안에서 일단 현재의 행과 열 개수를 세고,
그에 따라서 각 함수로 보냄 (R, C연산 둘 중 하나로)
그리고 나서 빈 자리..? 에 0 만큼 채워줌 -> 연산 함수에서는 0 제외하고 연산될 수 있도록 처리
time += 1 해주고 A[r][c]값 확인해주고 ...
배열이 무한정 ... 커지지 않게 100까지만 슬라이싱 해주고
출력 유의할 건 time이 101이 되는 순간 그냥 break 하고 print(-1) 해주면 됨

1907 구현)
레츠고 해봅시다
'''
def do_R():
    # 모든 행에 대해서 정렬 수행, [수, 등장 횟수] 를 모두 넣어줘야 함
    # 행 하나씩 뜯어보되, 하나씩 나오는 숫자를 nums에 빈도수 체크 해주고 그 빈도수가 적은 수 (1부터) idx랑 빈도수 tmp에 넣어주고 갈아끼우기
    for i in range(height):
        tmp = []
        nums = [0] * 101
        for j in range(len(arr[i])):
           arr_num = arr[i][j]
           nums[arr_num] += 1
        # 이 위치에 오면 행 하나 다 돈 거임. nums[n]이 적은 순부터 넣어줘야 함
        for n in range(1, 101):
            if nums[n] > 0:
                tmp.append((nums[n], n))
        tmp.sort()
        arr_tmp = []
        for cnt, number in tmp:
            arr_tmp.append(number)
            arr_tmp.append(cnt)
        arr[i] = arr_tmp

    maxj = 0
    # 가장 긴 행을 기준으로
    for i in range(height):
        maxj = max(maxj, len(arr[i]))

    # 위에서 maxj라는 변수로 가장 긴 열을 구해줬엉
    for i in range(height):
        if len(arr[i]) < maxj:
            for _ in range(maxj-len(arr[i])):
                arr[i].append(0)

    return


def do_C():
    global arr

    c_arr = list(map(list, zip(*arr)))
    for i in range(width):
        tmp = []
        nums = [0] * 101
        for j in range(len(c_arr[i])):
            arr_num = c_arr[i][j]
            nums[arr_num] += 1
        # 이 위치에 오면 행 하나 다 돈 거임. nums[n]이 적은 순부터 넣어줘야 함
        for n in range(1, 101):
            if nums[n] > 0:
                tmp.append((nums[n], n))
        tmp.sort()
        arr_tmp = []
        for cnt, number in tmp:
            arr_tmp.append(number)
            arr_tmp.append(cnt)
        c_arr[i] = arr_tmp

    maxj = 0
    for i in range(width):
        maxj = max(maxj, len(c_arr[i]))

    for i in range(width):
        if len(c_arr[i]) < maxj:
            for _ in range(maxj - len(c_arr[i])):
                c_arr[i].append(0)

    arr = [[0]*width for _ in range(maxj)]
    # 전치 행렬로 만들어줬던 거 다시 원래 배열대로 바꾼 뒤 덮어 씌워주기
    for i in range(width):
        for j in range(len(c_arr[i])):
            arr[j][i] = c_arr[i][j]
    return


R, C, K = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(3)]  # 초기 상태의 array
time = 0

while True:
    height = len(arr)  # 열의 길이
    width = len(arr[0])  # 행의 길이

    if height > R-1 and width > C-1:
        if arr[R-1][C-1] == K:
            break

    if height > 100:
        arr = arr[:100]
    if width > 100:
        arr = [row[:100] for row in arr]

    # 배열에 들어있는 수는 100보다 작거나 같은 자연수
    if height >= width:
        do_R()
    else:
        do_C()

    time += 1
    if time > 100:
        time = -1
        break

print(time)