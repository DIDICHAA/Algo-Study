total = int(input())
N = int(input())
tmp = 0

for i in range(N):
    price, ea = map(int, input().split())
    tmp += price*ea

if tmp == total: print('Yes')
else: print('No')