def do_cal(lst):
    global maxi, mini
    # + = * // 순서대로 1 2 3 4
    total = nums[0]
    j = 1

    for i in range(len(lst)):
        if lst[i] == 1:
            total += nums[j]
        elif lst[i] == 2:
            total -= nums[j]
        elif lst[i] == 3:
            total *= nums[j]
        else:
            if total < 0:
                tmp = abs(total) // nums[j]
                total = -tmp
            else:
                total //= nums[j]
        j += 1

    maxi = max(maxi, total)
    mini = min(mini, total)
    return


def make_p(cnt, lst):
    if cnt == N-1:
        do_cal(lst)
        return

    for i in range(len(ys_lst)):
        if not visited[i]:

            visited[i] = True
            lst.append(ys_lst[i])
            make_p(cnt+1, lst)
            lst.pop()
            visited[i] = False


N = int(input())
nums = list(map(int, input().split()))
yeonsan = list(map(int, input().split()))
maxi = -2e9
mini = 2e9
visited = [False]*(N-1)

# 각 연산자에 따라 1 2 3 4로 나눠서 리스트에 그 갯수만큼 새롭게 저장하고 이 리스트를 가지고 순열 백트래킹을 한다면 ..
ys_lst = []
for i in range(1, 5):
    n = yeonsan[i-1]
    if n > 0:
        for j in range(n):
            ys_lst.append(i)

make_p(0, [])
print(maxi, mini, sep='\n')