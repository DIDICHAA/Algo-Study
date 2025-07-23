N = int(input())
st = list(map(int, input().split()))

ans, tmp = 0, 0
for n in st:
    if n != 0:
        tmp += 1
        ans = max(ans, tmp)
    else:
        tmp = 0

print(ans)