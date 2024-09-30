'''
1410 문제 이해
블록은 검은색, 무지개, 일반 블록
일반 블록은 M가지 색상, 자연수로 표현
검은색 블록은 -1, 무지개 블록은 0
인접한 칸의 기준은 4방

블록 그룹은 연결된 블록의 집합, 그룹에는 일반 블록이 적어도 하나, 색은 모두 같아야 함
검은색은 포함X 무지개는 갯수 상관없이 포함 가능

그룹에 속한 블록의 개수는 2개 이상,

그룹에 속한 블록의 개수는 2개 이상,
임의의 한 블록에서 그룹에 속한 인접한 칸으로 이동해서
그룹에 속한 다른 모든 칸으로 이동할 수 있어야 한다

블록 그룹의 기준은 일반 블록 중에서 행의 번호, 열의 번호 순으로 가장 작은 블록

1. 크기가 가장 큰 블록 그룹, 여러 개라면 무지개 블록이 가장 많은 블록, 여러 개라면
    기준 블록의 행, 열 순으로 가장 큰 것
2. 1번에서 찾은 블록 그룹의 모든 블록 제거, 모든 블록의 수 ^ 2점 획득
3. 격자에 중력 작용
    -> 검은색 블록을 제외한 모든 블록이 행의 번호가 큰 칸으로 이동.
    이동은 다른 블록이나 격자의 경계를 만나기 전까지 반복 // 아래로 떨어짐
4. 격자가 반시계 90도 방향으로 회전
5. 격자에 중력 작용


1420 구상
1. 가장 큰 블록 그룹을 찾는 bfs
    -> 블록 그룹은 1~M까지의 자연수로 이루어져 있음.
    -> 그니까 0이랑 어떤 숫자 섞인, 근데 갯수가 가장 많은 거 찾으면 되는 거임
    -> 그 크기가 맥시멈인 게 여러 개일 떄, 가장 왼쪽 위에 있는 일반 블록의 좌표를
        같이 넣어야 sort 했을 때 비교 가능함
        -> 그룹이 확실시 되면 걔네를 싹 없애줌 -2 그냥 빈 칸으로 만들어줘야 함
        -> total += 칸의 개수 ** 2
2. 중력 작용 함수
    -> 행을 기준으로 해서 아래 -1이나 빈칸이 아닌 칸이 나올 때까지
        위의 숫자들을 아래로 내려줘야 함
        -> while문 돌려서 숫자 가장 아래쪽에 있는 것부터 차례로 내려주면 될 거 같음
3. 90도 반시계 방향으로 회전
    ** 이건 함수 말고 main while문에다가 빼주자 반시계 90도 코드 알지??

4. main
    -> main의 while문 종료 조건은 bfs에서 아무런 블록 그룹도 찾지 못했을 때임
        -> 블록 그룹의 조건은 일반 블록이 적어도 하나, 무지개색은 상관없고
            전체 갯수가 2개 이상이어야 함 그니까 bfs 돌았는데도 최대 블록그룹 개수가
            1이라면 더이상 찾을 블록 그룹이 없는 거니까 return에 -1 해주고 종료

1424 구현) 와자자 풀 수 있다!!
    1437. check point 1. find_block 잘 돌아가나요?
        -> 아니요 ;; 매우 이상합니다람쥐 아앗 나랑 같은 값이어야 한다는 조건을 안 넣어줌
        1439 해결!
    1444. 구현하다가 remove 함수를 따로 빼려면 bfs를 하나 더 쓰는 게 낫겠다는 생각..
        -> 설계 바꿔서 bfs 두 개인 걸로 구현 // 구현 완료 후 시간 초과 안 날 지 확인
    1453. remove_blocks 까지 일단 원하는 대로 돌아가셔요 / -2 처리해준 거 잊지 말기
    1503. check point 2. 대망의 중력... 전치 행렬로 구현 중인데 잘 움직이나요?
        -> 아뇨... 한 칸씩으로 보면 안 되고 될 때까지 가져가야 됨
        ** 오늘의 목표 내가 제대로 구현한 적 없는 이런 중력 어쩌고 녀석 구현해보기 **
        엥 된 거 같다 뭐지
    1519. 다 돌았는데도 종료 조건에 걸리지 않는 이슈 발생!! 화장실 다녀와서 처리할 거임
        -> 예상한 것보다 조금 더 돌아가는 거 같음 .. 흠 이유가 뭐지?
        예상) 처음에 없애는 bfs 처리할 때 자연수일 때만 시작하도록 했는데 ...
        뻥임 아닌 거 같음 sort 할 때 cnt를 가장 먼저 내세워야 하니까 cnt가 높은 순 ~ i가 작은 순..
        이렇게 가야 되는데 그냥 소트 때려버려서 cnt가 제일 크고, 그 다음에 i가 크고 .. 이렇게 됨
        황당함 -> i랑 j 넣을 때 - 붙여줌 그럼 sort 제대로 됨
    1528. 하지만 여전히 숫자가 조금 더 돌아감 1번 bfs 안에 문제가 있긴 한 듯
    !!!!! 0인 애들은 아래에서 탐색할 때 재방문 할 수도 있으므로 visited 처리를 다시 0으로 해줘야 함
        이거 고쳐도 테케는 틀림 근데 고쳤어야 했다!!!
        -> 마지막 gravity에서 예상값과 다르게 나옴 아마 -2 처리를 해주는 데 있어서 오류가 난 듯
            => 역시나 .. 1 2 -2 1 이런 식일 때 저 -2 1 2 1 이 되어야 하는데 2하고 -2만 swap
            -> 끝점에서부터 찾아주는 걸로 해야 할 듯
    1632. 중력 이슈 여전히 ...
        -> 지금까지의 내 접근 방식) 한 칸을 기준으로 접근하다 보니까 두 칸 이상 땡겨야 할 때
            오차가 발생함
            그래서 큰 while문 돌면서 조건 분기시켜주고, i랑 j를 각각 올려주는 식으로 하니까
            일단 테케 1, 3에서는 잘 돌아감 테케 2 왜 틀렸는지는 지금부터 알아봐야 함ㅋㅋ
            이번엔 뒤 쪽에서 제대로 안 움직이는 이슈가 발생함 모든 문제는 gravity로부터 ...

        issue 2. 테케 2번만 값이 틀림
        와 이것만 1시간 30분 팠는데 아직도 모름 야자 때 킵고잉 ㄱㄱ 오늘 안에 중력 어떻게 할 건지
        잡고 넘어갑시데잉 이건 풀고 가자링

'''
from collections import deque


def oob(i, j):
    return 0<=i<N and 0<=j<N


def find_block(si, sj, color):
    q = deque()
    visited[si][sj] = 1
    q.append((si, sj))
    tmp = [(si, sj)]
    cnt = 1
    while q:
        ci, cj = q.popleft()
        for di, dj in dir:
            ni, nj = ci+di, cj+dj
            if oob(ni, nj) and visited[ni][nj] == 0:
                if blocks[ni][nj] == color or blocks[ni][nj] == 0:
                    visited[ni][nj] = 1
                    q.append((ni, nj))
                    tmp.append((ni, nj))
                    cnt += 1   # 이번 칸에서 몇 개의 블록 그룹이 만들어 지는지 세 줄 거임
    o_cnt = 0
    for x, y in tmp:
        if blocks[x][y] == 0:
            visited[x][y] = 0
            o_cnt += 1

    return cnt, o_cnt


def remove_blocks(bsi, bsj):
    q = deque()
    color = blocks[bsi][bsj]
    visited = [[0]*N for _ in range(N)]
    visited[bsi][bsj] = 1
    q.append((bsi, bsj))

    tmp_lst = [[bsi, bsj]]
    while q:
        ci, cj = q.popleft()
        for di, dj in dir:
            ni, nj = ci+di, cj+dj
            if oob(ni, nj) and visited[ni][nj] == 0 and (blocks[ni][nj] == color or blocks[ni][nj] == 0):
                visited[ni][nj] = 1
                q.append((ni, nj))
                tmp_lst.append([ni, nj])

    for i, j in tmp_lst:
        blocks[i][j] = -2  # 빈 공간은 -2로 처리하고, 중력 이동 시 이를 고려해서 이동 시키는 수밖에..

    return


def gravity():
    global blocks

    tmp = [[-2 for _ in range(N)] for _ in range(N)]
    for j in range(N):
        idx = N-1
        q = deque()
        for i in range(N-1, -1, -1):
            if blocks[i][j] == -1:
                tmp[i][j] = -1
                while q:
                    num = q.popleft()
                    tmp[idx][j] = num
                    idx -= 1
                idx = i-1
            elif blocks[i][j] != -2:
                q.append(blocks[i][j])
        while q:
            num = q.popleft()
            tmp[idx][j] = num
            idx -= 1

    blocks = tmp
    return


N, M = map(int, input().split())
blocks = [list(map(int, input().split())) for _ in range(N)]
dir = [(0, 1), (0, -1), (1, 0), (-1, 0)]

total = 0  # 최종적으로 출력할 변수

while True:
    visited = [[0 for _ in range(N)] for _ in range(N)]
    max_cnt = 0

    # 여기에 무지개 블록의 수가 가장 많은 경우도 따져줘야 해서 i, j 뒤에 o_cnt도 포함 시켜줘야 함
    blocks_tmp = []
    for i in range(N):
        for j in range(N):
            if visited[i][j] == 0 and blocks[i][j] != -1 and blocks[i][j] != 0 and blocks[i][j] != -2:
                color = blocks[i][j]
                cnt, o_cnt = find_block(i, j, color)
                real_cnt = cnt-o_cnt
                if cnt >= 2 and real_cnt > 0:   # 블록 그룹이 만들어질 수 있다면
                    blocks_tmp.append([cnt, o_cnt, i, j])  # 정렬하기 위한 조건

    if not blocks_tmp:
        break

    blocks_tmp.sort(reverse=True)  # 가장 갯수가 많고 행 열 순으로 찾아줌
    tcnt, o_cnt, bsi, bsj = blocks_tmp[0]
    remove_blocks(bsi, bsj)
    total += tcnt ** 2

    gravity()
    blocks = list(map(list, zip(*blocks)))[::-1]
    gravity()

print(total)