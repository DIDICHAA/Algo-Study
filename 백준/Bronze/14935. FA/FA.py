x = int(input())
lst = list(map(int, str(x)))
leng = len(lst)

x = -1
flag = False
while 1:
    num = lst[0] * leng
    if x != num : x = num
    else:
        flag = True
        break

if flag: print('FA')
else: print('NFA')