'''
1600
* r과 c는 1에서부터 시작
* 초기에 모든 칸에는 양분이 5씩 들어있음

1. 봄 : 자신의 나이만큼 양분 +, 나이 + 1
    -> 각각의 나무는 나무가 있는 칸의 양분만 먹을 수 있음
    -> 하나의 칸에 여러 개의 나무 // 어린 나무부터 양분 먹음
    -> 만약 양분이 부족해서 나이만큼 양분을 못먹으면 즉사

2. 여름 : 봄에 죽은 나무가 양분이 됨
    -> 각각의 죽은 나무마다 나이를 2로 나눈 값이 양분으로 추가 됨 (int)

3. 가을 : 나무의 나이가 5의 배수일 때 나무 번식
    - 인접한 8개의 칸에 나이가 1인 나무가 생김 (oob안에서만)

4. 겨울 : S2D2가 땅을 돌아다니며 양분 추가
    -> 각 칸에 추가되는 양분의 양은 A[r][c] // 입력값

k년이 지난 후, 상도의 땅에 살아있는 나무의 개수를 구하시오!

구상
유의) 2차원 배열을 너무 많이 만들지 말 것. 입력 배열로 할 수 있는 것 고민
유의2) 정원과 동일한 사이즈의 2차원 배열을 만든 뒤, 파이어볼처럼 튜플로 관리
빡구현의 느낌이 오죠? 가보자고요
봄 / 여름 / 가을 / 겨울에 해당하는 함수를 만들고,
모든 계절을 한 번씩 돌았을 때 K -= 1해주는 while문을 main에 선언

1641 디버깅 // 각 함수 별로 체크포인트 만들어서 돌기
~ 이슈 정리 ~
1. 죽었어야 할 나무가 죽지 않음 / 아마도 pop부분이 잘못되지 않았을까? 하는 의심
    => 1년 지나고 나이 먹어야 되는데 나이를 안 먹음;;

2. winter의 91번째 라인에서 나이를 안 먹는 이슈가 발생 -> 해결

3. 구현에서의 문제!! 빈 리스트를 3차원 배열로 만들어놓고 나는 2차원 배열로 돌려서
    for문에 따른 주솟값을 제대로 못찾고 헤매이고 있음
    -> for tree in trees[i][j]를 그냥 k로 바꿔서 쓰고 해결

4. 역시나 ... remove를 쓰면 안 될 것 같아서(시간 복잡도) pop을 하려고 했는데
이상하게 돌아가는 것 같아서 확인해보니 죽는 녀석들이 항상 맨 앞에 (pop(-1))에 있는 건 아니라
죽어야 할 녀석들이 이상하게 빠지고 있었음 파이어볼처럼 덮어 씌우거나 ㅎㅎ; for문으로 없애줘야 할 듯

5. tc 4번부터 답이 안 맞아서 디버깅 필요 / 아마도? fake_trees에 이상한 값이 들어가고 있는 게 아닐까 하는 의심
    ->
'''
def oob(i, j):
    return 0<=i<N and 0<=j<N

def spring():
    global trees
    # trees에 들어간 나이와 같게 nutrition에서 양분 -=
    # 만약 하나의 trees 칸에 여러 개의 나무가 있다면 더 나이가 적은 것부터 양분 먹음
    # 만약 양분이 부족하다면, 양분 안 줄어들고 나무 즉사

    dead = []
    fake_trees = [[[] * N for _ in range(N)] for _ in range(N)]
    cnt = 0  # 한 그루라도 죽었다면 두 배열에 차이가 생기니 덮어 씌워주고, 아니라면 그냥 킵고잉

    for i in range(N):
        for j in range(N):
            if len(trees[i][j]) == 0: continue
            else:
                trees[i][j].sort()
                for k in range(len(trees[i][j])):
                    # 나무가 있는 영양분의 좌표에 나무의 나이만큼 영양분 빼줌
                    if nutrition[i][j] >= trees[i][j][k]:
                        nutrition[i][j] -= trees[i][j][k]
                        trees[i][j][k] += 1
                        fake_trees[i][j].append(trees[i][j][k])
                    else:
                        nut = trees[i][j][k] // 2
                        dead.append((i, j, nut))
                        cnt += 1

    # 다 나온 다음에 여기서 죽은 녀석들을 담아두고 한 번에 뺴줘야 할 듯
    if cnt > 0:
        trees = fake_trees

    summer(dead)

def summer(lst):
    # 여름에 죽은 나무가 양분이 되는 계절
    # 각각의 죽은 나무의 나이를 // 2로 나눈 값이 양분으로 추가
    # 이걸 spring에서 받아와서 처리하는 것이 ...

    for dead in lst:
        i, j, nut = dead
        nutrition[i][j] += nut

    autumn()


def autumn():
    # trees에 들어가 있는 나이들이 5의 배수일 때 나무가 8방 번식
    # 이 때 age가 1인 녀석들이 추가 됨
    # oob 확인 필요
    for i in range(N):
        for j in range(N):
            for k in range(len(trees[i][j])):
                if trees[i][j][k] % 5 != 0: continue
                else:
                    for di, dj in dir:
                        ni, nj = i+di, j+dj
                        if oob(ni, nj):
                            trees[ni][nj].append(1)
    winter()


def winter():
    for i in range(N):
        for j in range(N):
            nutrition[i][j] += add[i][j]
    return


N, M, K = map(int, input().split())
nutrition = [[5]*N for _ in range(N)]  # 초기 영양분
add = [list(map(int, input().split())) for _ in range(N)]
trees = [[[]*N for _ in range(N)] for _ in range(N)]


dir = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]

for _ in range(M):
    x, y, age = map(int, input().split())
    trees[x-1][y-1].append(age)

# nutrition의 값은 각 x, y 위치에 따라 겨울마다 추가되는 양분의 값!
while K > 0:
    spring()

    K -= 1

# trees에 값이 있다는 것, 살아있다는 것 ...
total = 0
for i in range(N):
    for j in range(N):
        for k in range(len(trees[i][j])):
            if trees[i][j][k]:
                total += 1

print(total)