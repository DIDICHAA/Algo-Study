num, sco = 0, 0

for i in range(5):
    a, b, c, d = map(int, input().split())
    tmp = a+b+c+d
    if tmp > sco:
        sco = tmp
        num = i+1
    else: continue

print(num, sco)