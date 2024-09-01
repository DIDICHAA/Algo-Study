A = list(map(int, input()))
B = list(map(int, input()))

phone = []
for i in range(8):
    n = A[i]
    m = B[i]
    phone.append(A[i])
    phone.append(B[i])

for i in range(1, len(phone)):
    n = (phone[i] + phone[i-1]) % 10
    phone[i-1] = n
phone.pop(-1)

while True:
    for i in range(1, len(phone)):
        phone[i-1] = (phone[i] + phone[i-1]) % 10

    phone.pop(-1)

    if len(phone) == 2:
        break

for n in phone:
    print(n, end="")