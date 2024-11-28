def check(lst):
    temp_num = int(''.join(lst))

    for i in range(2, temp_num//2+1):
        if temp_num % i == 0:
            return False
    return True


def make_p(cnt, lst):
    if cnt == N:
        print(''.join(lst))
        return

    for i in range(10):
        lst.append(nums[i])

        if lst[0] not in '2357':
            lst.pop()
            continue

        if lst and not check(lst):
            lst.pop()
            continue

        make_p(cnt+1, lst)
        lst.pop()


N = int(input())
nums = '1234567890'
make_p(0, [])