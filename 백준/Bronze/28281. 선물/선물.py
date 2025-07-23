N, X = map(int, input().split())
price = list(map(int, input().split()))

find_day = 2001
for n in range(len(price)-1):
    if price[n] + price[n+1] < find_day:
        find_day = price[n] + price[n+1]

print(X*find_day)