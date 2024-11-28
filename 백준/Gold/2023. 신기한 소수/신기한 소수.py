def check(lst):
    temp_num = ''
    for n in lst:
        temp_num += str(n)

    temp_num = int(temp_num)

    for i in range(2, temp_num//2+1):
        if temp_num % i == 0:
            return False
    return True


def make_p(cnt, lst):
    if cnt == N:
        new_num = ''
        for n in lst:
            new_num += str(n)
        print(new_num)
        return

    for i in range(10):
        lst.append(nums[i])

        if lst[0] == 0 or lst[0] == 1:
            lst.pop()
            continue

        if lst and not check(lst):
            lst.pop()
            continue

        make_p(cnt+1, lst)
        lst.pop()


N = int(input())
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
make_p(0, [])