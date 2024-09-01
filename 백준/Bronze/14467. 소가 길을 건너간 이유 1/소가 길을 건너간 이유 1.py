N = int(input())
cows = [-1]*10

total = 0
for _ in range(N):
    cow, d = map(int, input().split())
    if cows[cow-1] == -1:
        cows[cow-1] = d

    elif cows[cow-1] != -1 and cows[cow-1] != d:
        cows[cow-1] = d
        total += 1

print(total)