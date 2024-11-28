def check(lst):
    temp_num = ''
    for n in lst:
        temp_num += str(n)

    if temp_num[0] == '0' or temp_num[0] == '1':
        return False

    temp_num = int(temp_num)
    for i in range(2, temp_num):
        if temp_num % i == 0:
            return False
    return True


def make_comb(cnt, lst):
    if cnt == N:
        new_num = ''
        for n in lst:
            new_num += str(n)
        ans_lst.append(int(new_num))
        return

    for i in range(10):
        lst.append(nums[i])
        
        if lst and not check(lst):
            lst.pop()
            continue

        make_comb(cnt+1, lst)
        lst.pop()


N = int(input())
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
ans_lst = []
make_comb(0, [])
visited = [False] * 11
for n in ans_lst:
    print(n, end='\n')
