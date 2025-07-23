N = int(input())
price = int(input())

tmp1 = price - 500
tmp2 = int(price * 0.9)
tmp3 = price - 2000
tmp4 = int(price * 0.75)

if 4 < N < 10:
    price = tmp1

elif 9 < N < 15:
    price = min(tmp1, tmp2)

elif 14 < N < 20:
    price = min(tmp1, tmp2, tmp3)

elif N >= 20:
    price = min(tmp1, tmp2, tmp3, tmp4)

if price < 0 : print(0)
else: print(price)