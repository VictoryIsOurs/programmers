def solution(brown, yellow):
    answer = []
    check = [False] * (yellow+1)
    div = []
    for i in range(1, yellow+1):
        if yellow % i == 0 and not check[i]:
            check[i] = True
            check[yellow//i] = True
            div.append(i)
    for h in div:
        w = yellow // h
        if ((w+2)*(h+2) - w*h) == brown:
            answer.append(w+2)
            answer.append(h+2)
            break
    return answer