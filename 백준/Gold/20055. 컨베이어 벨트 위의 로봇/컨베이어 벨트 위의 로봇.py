'''
[ 문제 풀기 전 마음가짐 ]
** 문제에서 요구하는 그대로 구현할 것 **
** 인덱스 유의하면서 풀 것 **
** 거시적으로 내 코드 흐름 보기 **
** 시간 체크 하면서 풀어보기 **

1355 문제 이해
< 조건 >
1. 언제든지 로봇이 내리는 위치에 도달하면 즉시 내림
2. 로봇은 벨트 위에서 스스로 이동할 수 있음
3. 로봇을 올리는 위치에 올리거나 어떤 칸으로 이동하면 그 칸의 내구도는 즉시 -= 1

< 순서 >
1. 벨트가 각 칸에 있는 로봇과 함께 한 칸 씩 회전
2. 가장 먼저 벨트에 올라간 로봇부터 벨트가 회전하는 방향으로 한 칸 이동 가능 시 이동
    -> 이동 불가능할 시 가만히 있음
    -> 로봇이 없고, 내구도가 1 이상이어야 이동 가능
3. 올리는 위치에 있는 칸의 내구도가 0이 아니면 올리는 위치에 로봇 올림
4. 내구도가 0인 칸의 개수가 K개 이상일 시 과정 종료, 아니라면 1번 반복

출력 : 종료 시 몇 번째 단계가 진행 중이었는가?

1400 구상
문제에서 주어진 그대로 구현!!
rotate_belt, move_robot에서 벨트나 로봇이 내리는 위치에 존재하는 경우 없애는 로직 추가해줘야 함

'''
def rotate_belt():
    global robots, belt
    # 벨트가 이동할 때는 내구도 감소 없음
    tmp_lst = [0]*(2*N)
    tmp_rbt = [0]*(2*N)
    for i in range(1, len(belt)):
        tmp_lst[i] = belt[i-1]
        tmp_rbt[i] = robots[i-1]
    tmp_lst[0] = belt[-1]
    tmp_rbt[0] = robots[-1]

    belt = tmp_lst
    robots = tmp_rbt

    if robots[N-1] != 0:
        robots[N-1] = 0  # 벨트가 다 돌고 나서 내리는 위치에 로봇이 있다면 ...

    return

# 이거 역순으로 안 해주면 로봇 하나가 지구 끝까지 돈다 .. ; 유의해
def move_robot():
    global robots, belt
    for i in range(len(robots)-1, -1, -1):
        if robots[i] == 0:
            if robots[i-1] != 0 and belt[i] > 0:
                robots[i], robots[i-1] = robots[i-1], robots[i]
                belt[i] -= 1  # 내구도 감소

    if robots[N-1] != 0:
        robots[N-1] = 0  # 로봇 안뇽
    return


def on_robot():
    global robots, belt
    if belt[0] != 0:
        robots[0] += 1
        belt[0] -= 1
    return


def check_naegudo():
    cnt = 0
    for i in range(len(belt)):
        if belt[i] == 0:
            cnt += 1

    if cnt >= K:
        return False
    return True


N, K = map(int, input().split())
belt = list(map(int, input().split()))
robots = [0]*(2*N)
step = 0

while True:
    step += 1
    rotate_belt()
    move_robot()
    on_robot()
    flag = check_naegudo()
    if not flag:
        break

print(step)