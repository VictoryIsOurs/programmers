def solution(enter, leave):
    q, n, dt = [], len(enter), {}
    for i in range(1, n+1):
        dt[str(i)] = 0
    for l in leave:
        if l not in q:
            cnt = 0
            while l not in q:
                q.append(enter.pop(0))
                cnt += 1
            for x in q:
                if dt[str(x)] == 0:
                    dt[str(x)] += len(q) - 1
                else:
                    dt[str(x)] += cnt
            q.pop()
        else:
            q.remove(l)
    return list(dt.values())