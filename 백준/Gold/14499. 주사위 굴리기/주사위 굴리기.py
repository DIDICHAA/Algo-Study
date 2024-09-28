'''
문제 이해)
N*M 크기의 지도

초기 주사위 상태)
윗면이 1, 동쪽 방향에 3

주사위 굴리고 이동
-> 이동한 칸에 0이 쓰여 있으면
    -> 주사위 바닥에 쓰인 숫자가 칸에 복사
-> 이동한 칸에 0이 아닌 수가 쓰여 있으면
    -> 칸의 숫자가 주사위 바닥으로 복사
    -> 칸은 0이 됨

주사위 이동 시, 상단에 쓰여있는 숫자를 매번 출력
주사위 배열을 만들어두고, 어떤 숫자가 들어와서 그 숫자가 업데이트 되면
그 반대편의 숫자를 출력하는 로직

동1 서2 북3 남4
주사위는 결국 command에 따라 이동

주사위가 단순히 사방으로 움직이는 게 아니라,
정육면체가 각 면을 닿게 하며 움직임을 고려
초기 주사위는 전부 0으로 설정 돼 있음
'''
# 주사위를 굴리고 이동했을 때 6면이 각 command에 따라서 바뀜
def change_dice(com):
    if com == 1: # 동쪽으로 이동할 때
        dice[3], dice[4], dice[5], dice[6] = dice[5], dice[6], dice[4], dice[3]
    elif com == 2:  # 서쪽으로 이동할 때
        dice[3], dice[4], dice[5], dice[6] = dice[6], dice[5], dice[3], dice[4]
    elif com == 3:  # 북쪽으로 이동할 때
        dice[1], dice[2], dice[5], dice[6] = dice[5], dice[6], dice[2], dice[1]
    else:  # 남쪽으로 이동할 때
        dice[1], dice[2], dice[5], dice[6] = dice[6], dice[5], dice[1], dice[2]


def copy_dice(i, j):
        if arr[i][j] == 0:
            arr[i][j] = dice[5]
        else:
            dice[5] = arr[i][j]
            arr[i][j] = 0


def move_dice(i, j):
    for command in commands:
        di, dj = dir[command-1]
        ni, nj = i+di, j+dj

        if 0<=ni<N and 0<=nj<M:  # 범위 안에서만 주사위가 움직임
            change_dice(command)
            copy_dice(ni, nj)
            i, j = ni, nj  # 주사위가 있는 위치 옮겨줌
            print(dice[6])
        else:
            continue


N, M, x, y, K = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
commands = list(map(int, input().split()))

dir = [(0, 1), (0, -1), (-1, 0), (1, 0)]
dice = [0]*7  # 1번 인덱스부터 상하좌우나맞 순서

move_dice(x, y)