from itertools import permutations


def solution(n, weak, dist):
    answer = 1e9

    new_weak = weak[:]
    for i in range(len(weak)):
        new_weak.append(weak[i] + n)
        
    cases = list(permutations(dist, len(dist)))

    for s in range(len(weak)):
        for case in cases:
            cnt, now = 1, s
            for i in range(1, len(weak)):
                next = s+i
                where = new_weak[next] - new_weak[now]
                if where > case[cnt-1]:
                    now = next
                    cnt += 1
                    if cnt > len(dist): break

            if cnt <= len(dist):
                answer = min(answer, cnt)

    return answer if answer != 1e9 else -1
