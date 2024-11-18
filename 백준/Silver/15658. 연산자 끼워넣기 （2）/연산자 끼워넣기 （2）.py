def dfs(idx, res):
    global max_sum, min_sum

    if idx == N-1:
        max_sum = max(max_sum, res)
        min_sum = min(min_sum, res)
        return

    for i in range(4):
        if tmp[i] <= 0: continue
        tmp[i] -= 1
        if i == 0:
            dfs(idx+1, res+nums[idx+1])
        elif i == 1:
            dfs(idx+1, res-nums[idx+1])
        elif i == 2:
            dfs(idx+1, res*nums[idx+1])
        else:
            dfs(idx+1, int(res/nums[idx+1]))

        tmp[i] += 1


N = int(input())
nums = list(map(int, input().split()))
tmp = list(map(int, input().split()))
max_sum, min_sum = -2e9, 2e9

dfs(0, nums[0])
print(max_sum, min_sum, sep="\n")