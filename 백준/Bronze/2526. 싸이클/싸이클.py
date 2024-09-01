N, P = map(int, input().split())

nums = []
x = N
while True:
    x = x*N % P

    if x in nums:
        break

    else:
        nums.append(x)

print(len(nums)-nums.index(x))