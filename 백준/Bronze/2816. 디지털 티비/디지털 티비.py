N = int(input())
channels = list(input() for _ in range(N))
ans = []
c = 0

while channels[c] != 'KBS1':
    c += 1
    ans.append(1)

for _ in range(c):
    ans.append(4)

c = 0
channels.remove('KBS1')
channels = ['KBS1'] + channels

while channels[c] != 'KBS2':
    c += 1
    ans.append(1)
for _ in range(c-1):
    ans.append(4)

print("".join(map(str, ans)))