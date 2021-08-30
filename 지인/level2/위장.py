def solution(clothes):
    closet = {}
    for c in clothes:
        if c[1] in closet:
            closet[c[1]] += 1
        else:
            closet[c[1]] = 1
    res = 1
    for k, v in closet.items():
        res *= (v + 1)

    return res - 1