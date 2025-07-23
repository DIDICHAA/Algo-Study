N = int(input())
vote = list(map(int, input().split()))

c, b, k = 0, 0, 0
for n in vote:
    if n == 0:
        k += 1
    elif n == 1:
        c += 1
    else:
        b += 1

if k != 0 and N//2 <= k:
    print('INVALID')
elif b >= c:
    print('REJECTED')
else:
    print('APPROVED')