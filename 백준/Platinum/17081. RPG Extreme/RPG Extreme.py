def iob(i, j):
    return 0<=i<N and 0<=j<M


def check_health():
    if my_info[0] <= 0:
        return False
    return True


def check_exp():
    if my_info[5] >= my_info[4]*5:
        my_info[1] += 5  # 총 체력 상승
        my_info[0] = my_info[1]  # 체력 회복
        my_info[2] += 2  # 공격력 상승
        my_info[3] += 2  # 방어력 상승
        my_info[5] = 0  # 경험치는 다시 0
        my_info[4] += 1  # 레벨업!
    return


def move():
    global status, survived_flag, jewerly
    global si, sj

    di, dj = DIR_DICT[command]
    ni, nj = si + di, sj + dj
    if not iob(ni, nj) or board[ni][nj] == '#':
        if board[si][sj] == '^':
            if 'DX' in jewerly:
                my_info[0] -= 1
            else:
                my_info[0] -= 5
            if my_info[0] <= 0:
                if 'RE' in jewerly:
                    tmp = []
                    for n in range(len(jewerly)):
                        if jewerly[n] == 'RE': continue
                        tmp.append(jewerly[n])
                    jewerly = tmp
                    my_info[0] = my_info[1]
                    si, sj = rsi, rsj
                    return 1, si, sj
                else:
                    survived_flag = False
                    status = 'YOU HAVE BEEN KILLED BY SPIKE TRAP..'
                    return 2, si, sj
        else:
            return 1, si, sj
    if iob(ni, nj) and board[ni][nj] != '#':
        return 0, ni, nj
    else:
        return 1, si, sj


def trap():
    global status, survived_flag, jewerly
    global si, sj

    if 'DX' in jewerly:
        my_info[0] -= 1
    else:
        my_info[0] -= 5

    if my_info[0] <= 0:
        if 'RE' in jewerly:
            tmp = []
            for n in range(len(jewerly)):
                if jewerly[n] == 'RE': continue
                tmp.append(jewerly[n])
            jewerly = tmp
            my_info[0] = my_info[1]
            si, sj = rsi, rsj
        else:
            survived_flag = False
            status = 'YOU HAVE BEEN KILLED BY SPIKE TRAP..'
    return


def get_item():
    global attack_item, defense_item

    board[si][sj] = '.'
    what, S = items[si][sj]

    if what == 'W':
        attack_item = int(S)

    elif what == 'A':
        defense_item = int(S)

    else:
        if S in jewerly or len(jewerly) == 4:
            return
        jewerly.append(S)
    return


def attack_monster(ti, tj):
    global status, is_boss_die, jewerly
    global si, sj
    global survived_flag

    name, m_attack, m_defense, m_hp, mr_hp, exp = monsters[ti][tj]
    my_hp, my_attack, my_defense = my_info[0], my_info[2]+attack_item, my_info[3]+defense_item

    if board[ti][tj] == 'M' and 'HU' in jewerly:
        my_info[0] = my_info[1]

    winner = False
    fight_turn = 1
    while 1:
        if fight_turn == 1 and 'CO' in jewerly:
            if 'DX' in jewerly:
                monsters[ti][tj][3] -= max(1, my_attack*3 - m_defense)
            else:
                monsters[ti][tj][3] -= max(1, my_attack*2 - m_defense)
        else:
            monsters[ti][tj][3] -= max(1, my_attack - m_defense)

        if monsters[ti][tj][3] <= 0:
            winner = True
            break

        if fight_turn == 1 and 'HU' in jewerly and board[ti][tj] == 'M':
            pass
        else:
            my_info[0] -= max(1, m_attack - my_defense)

        if my_info[0] <= 0:
            break
        fight_turn += 1

    if winner:
        if 'EX' in jewerly:
            my_info[5] += int(exp*1.2)
        else:
            my_info[5] += exp
        check_exp()

        if 'HR' in jewerly:
            if my_info[0] + 3 <= my_info[1]:
                my_info[0] += 3
            else:
                my_info[0] = my_info[1]

        if board[ti][tj] == 'M':
            status = 'YOU WIN!'
            is_boss_die = True
        si, sj = ti, tj
        board[ti][tj] = '.'

    else:
        if 'RE' in jewerly:
            tmp = []
            for n in range(len(jewerly)):
                if jewerly[n] == 'RE': continue
                tmp.append(jewerly[n])
            jewerly = tmp
            my_info[0] = my_info[1]
            monsters[ti][tj][3] = mr_hp
            si, sj = rsi, rsj
        else:
            survived_flag = False
            status = 'YOU HAVE BEEN KILLED BY ' + name + '..'

    return


N, M = map(int, input().split())
board = [list(map(str, input())) for _ in range(N)]
K, L = 0, 0
for i in range(N):
    for j in range(M):
        if board[i][j] == '&':
            K += 1
        elif board[i][j] == 'M':
            K += 1
        elif board[i][j] == 'B':
            L += 1
        elif board[i][j] == '@':
            si, sj = i, j
            rsi, rsj = i, j
            board[i][j] = '.'

commands = list(map(str, input()))
monsters = [[[] for _ in range(M)] for _ in range(N)]
items = [[[] for _ in range(M)] for _ in range(N)]
DIR_DICT = {
    'L':(0, -1),
    'R':(0, 1),
    'U':(-1, 0),
    'D':(1, 0)
}

for _ in range(K):
    R, C, S, W, A, H, E = map(str, input().split())
                                    # 이름, 공격력, 방어력, 현재 체력, 최대 체력, 경험치
    monsters[int(R)-1][int(C)-1] = [S, int(W), int(A), int(H), int(H), int(E)]

for _ in range(L):
    R, C, T, S = map(str, input().split())
    items[int(R)-1][int(C)-1] = [T, S]

# now HP, whole HP, attack, defense, LV, EXP
my_info = [20, 20, 2, 2, 1, 0]
attack_item, defense_item, jewerly = 0, 0, []
status = ''  # if i die, the reason why
is_boss_die = False
survived_flag = True

turn = 0
for command in commands:
    sta, ni, nj = move()
    turn += 1

    if sta == 1: continue  # 이 두 케이스는 위치 변경 없음
    elif sta == 2: break

    if board[ni][nj] == '.':
        si, sj = ni, nj
    elif board[ni][nj] == '^':
        si, sj = ni, nj
        trap()
    elif board[ni][nj] == 'B':
        si, sj = ni, nj
        get_item()
    elif board[ni][nj] == '&' or board[ni][nj] == 'M':
        attack_monster(ni, nj)

    if not check_health():
        break

    if is_boss_die:
        break

if status == '':
    status = 'Press any key to continue.'

if survived_flag:
    board[si][sj] = '@'
for lst in board:
    for n in lst:
        print(n, end='')
    print()
print(f'Passed Turns : {turn}')
print(f'LV : {my_info[4]}')
if my_info[0] < 0:
    my_info[0] = 0
print(f'HP : {my_info[0]}/{my_info[1]}')
print(f'ATT : {my_info[2]}+{attack_item}')
print(f'DEF : {my_info[3]}+{defense_item}')
print(f'EXP : {my_info[5]}/{my_info[4]*5}')
print(status)