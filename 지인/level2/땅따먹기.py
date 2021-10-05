def solution(land):

    for i in range(1, len(land)):
        for j in range(4):
            mx = -1
            for k in range(4):
                if k != j:
                    mx = max(mx, land[i-1][k])
            land[i][j] += mx

    return max(land[len(land)-1])