def convert(n, num):
    if num == 0: 
        return '0'
    else:
        res = ''
        dt = {10: 'A', 11: 'B', 12: 'C', 13: 'D', 14: 'E', 15: 'F'}
        while num > 0:
            rem = num % n
            if rem >= 10: 
                res += dt[rem]
            else: 
                res += str(rem)
            num //= n
        return res[::-1]
    
def solution(n, t, m, p):
    ans, answer, idx = '', '', 0
    while len(ans) < t*m:
        ans += convert(n, idx)
        idx += 1
    for i in range(len(ans)):
        if i % m == 0:
            answer += ans[i+p-1]
        if len(answer) == t:
            break
    return answer