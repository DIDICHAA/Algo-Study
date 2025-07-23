word_lst = [ord('M')-65, ord('O')-65, ord('B')-65, ord('I')-65, ord('S')-65]
check_lst = [0]*26
word = list(map(str, input()))

flag = True
for n in word:
    check_lst[ord(n)-65] += 1

for m in word_lst:
    if check_lst[m] == 0:
        flag = False
        break

if flag: print('YES')
else: print('NO')