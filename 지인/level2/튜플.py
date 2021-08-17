def solution(s):
    answer = []
    s = s[1:len(s)-1]
    indices = []
    for i in range(len(s)):
        if s[i] == ',' and s[i-1] == '}' and s[i+1] == '{':
            indices.append(i)

    if len(indices) == 0:
        answer.append(s)
    elif len(indices) == 1:
        answer.append(s[:indices[0]])
        answer.append(s[indices[0]+1:])
    else:
        answer.append(s[:indices[0]])
        for i in range(len(indices)-1):
            answer.append(s[indices[i]+1:indices[i+1]])
        answer.append(s[indices[-1]+1:])

    res = []
    for ans in answer:
        tmp = ans[1:len(ans)-1].split(',')
        res.append(set(tmp))
    res.sort(key = lambda x:len(x))

    final = set()
    total = []
    for r in res:
        diff = r.difference(final)
        final.update(diff)
        total.append(list(diff))

    total = sum(total, [])
    total = list(map(int, total))
    return total

'''
다른 사람 코드

def solution(s):
    answer = []

    s1 = s.lstrip('{').rstrip('}').split('},{')

    new_s = []
    for i in s1:
        new_s.append(i.split(','))

    new_s.sort(key = len)

    for i in new_s:
        for j in range(len(i)):
            if int(i[j]) not in answer:
                answer.append(int(i[j]))

    return answer
'''