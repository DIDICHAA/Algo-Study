def check(lst):
    temp_num = int(''.join(lst))

    for i in range(2, temp_num//2+1):
        if temp_num % i == 0:
            return False
    return True


def make_p(num, cnt):
    if cnt == N:
        print(num)
        return

    for i in range(5):
        num += nums[i]

        if not check(num):
            num = num[:-1]
            continue

        make_p(num, cnt+1)
        num = num[:-1]


N = int(input())
nums = '13579'
for n in '2357':
    make_p(n, 1)