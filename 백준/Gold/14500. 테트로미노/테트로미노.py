'''
[ 마음 가짐 ]
** ........이런 유현 문제 싫지만 좋아해보자.....**
** ... 읽기 싫지만 꼼꼼히 읽어보자 .... **

1456 문제 이해
1. 인접한 칸이어야 한다, 팔방은 안 되고 사방으로 연결
2. 테트로미노를 하나 .. 놓아서 그 칸 안에 있는 합이 최대인... 회전 대칭 가능.... 회전까지는 이해해보겠는데 대칭은 대체 왜

1458 문제 구상 및 아이디어 내보기
1. 각 테트로미노마다 일단 자리 인덱스 룩업 테이블 만들어두기
    -> 1자 모양인 애는 ㅡ랑 ㅣ 이렇게 두 개고
    -> 네모 모양은 하나고
    -> L자 모양은 회전한 모양 합해서 4개, 반대로 뒤집어서 회전한 모양 4개 해서 총 8개 나올 듯
    -> 꾸부러진 모양은 총 4개
    -> ㅗ 모양은 회전한 모양 4개만 나옴
2. 어허 .. 각 모양마다 함수 만들어서 모양 만들고 각각 돌리고 그 모양에 맞게 종이 위에 올려가며 최댓값 갱신해야 되나
_2붙은 애들만 4방향 회전 시켜주면 됨.............. 그냥 다 적을까 ... 휴
zzzㅋㅋㅇㅏ 이렇게 하는 거 맞냐고요 ㅠㅠ 룩업 테이블이 오만 개가 나오는데 속도는 빠르것네 ...;

'''
def oob(i, j):
    return 0<=i<N and 0<=j<M

def do_cal():
    global max_sum

    for n in range(len(dict)):
        shape = dict[n]
        for i in range(N):
            for j in range(M):
                total = 0
                flag = True
                for di, dj in shape:
                    ni, nj = di+i, dj+j
                    if not oob(ni, nj):
                        flag = False
                        break
                    total += paper[ni][nj]
                if flag:
                    max_sum = max(max_sum, total)

    return


N, M = map(int, input().split())
paper = [list(map(int, input().split())) for _ in range(N)]

max_sum = 0  # 최댓값으로 갱신해줄 변수

square = [(0, 0), (0, 1), (1, 0), (1, 1)]

L_shape = [(0, 0), (1, 0), (2, 0), (2, 1)]
L_shape1 = [(0, 0), (0, 1), (0, 2), (1, 0)]
L_shape2 = [(0, 0), (0, 1), (1, 1), (2, 1)]
L_shape3 = [(0, 2), (1, 0), (1, 1), (1, 2)]

# 위에 녀석 대칭한 거
L_shape_2 = [(2, 0), (2, 1), (1, 1), (0, 1)]
L_shape_2_1 = [(0, 0), (1, 0), (1, 1), (1, 2)]
L_shape_2_2 = [(0, 0), (0, 1), (1, 0), (2, 0)]
L_shape_2_3 = [(0, 0), (0, 1), (0, 2), (1, 2)]

zigzag = [(0, 0), (1, 0), (1, 1), (2, 1)]
zigzag_1 = [(1, 0), (1, 1), (0, 1), (0, 2)]

zigzag_2 = [(0, 1), (1, 1), (1, 0), (2, 0)]
zigzag_3 = [(0, 0), (0, 1), (1, 1), (1, 2)]

beobgyu = [(0, 0), (0, 1), (0, 2), (1, 1)]
beobgyu_2 = [(0, 1), (1, 0), (1, 1), (2, 1)]
beobgyu_3 = [(0, 1), (1, 0), (1, 1), (1, 2)]
beobgyu_4 = [(0, 0), (1, 0), (1, 1), (2, 0)]

ilja = [(0, 0), (0, 1), (0, 2), (0, 3)]
ilja_2 = [(0, 0), (1, 0), (2, 0), (3, 0)]

dict = {0:L_shape, 1:L_shape1, 2:L_shape2, 3:L_shape3,
        4:L_shape_2, 5:L_shape_2_1, 6:L_shape_2_2, 7:L_shape_2_3,
        8:zigzag, 9:zigzag_1, 10:zigzag_2, 11:zigzag_3, 12:beobgyu,
        13:ilja, 14:ilja_2, 15:square, 16:beobgyu_2, 17:beobgyu_3, 18:beobgyu_4}
do_cal()
print(max_sum)