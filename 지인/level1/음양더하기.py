def solution(a, signs):
    answer = 0
    for i in range(len(a)):
        if signs[i]:
            answer += a[i]
        else:
            answer += (-1) * a[i]
    return answer