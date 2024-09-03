def make_p(cnt, lst):
    global ans

    if cnt == len(X_):
        num = int(''.join(lst))
        ans.append(num)
        return

    for i in range(len(X_)):
        if visited[i] == 0:
            visited[i] = 1

            lst.append(X_[i])
            make_p(cnt+1, lst)
            lst.pop()

            visited[i] = 0


X = input()
X_ = list(X)
X_.sort()
ans = []
visited = [0] * len(X_)

# X로 백트래킹해서 만들 수 있는 조합 중 가장 가장 작은 녀석
make_p(0, [])
ans = set(ans)

X = int(X)
tmp = []
for n in ans:
    if n > X:
        tmp.append(n)

if len(tmp) == 0:
    print(0)
else:
    tmp.sort()
    print(tmp[0])