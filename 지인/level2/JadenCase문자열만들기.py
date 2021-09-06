def solution(s):
    answer = ''
    s = s.lower()
    for i in range(len(s)):
        if i == 0:
            answer += str(s[i]).upper()
        else:
            if s[i].islower() and s[i-1] == ' ':
                answer += str(s[i]).upper()
            else:
                answer += s[i]
    return answer