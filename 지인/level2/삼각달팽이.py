def solution(n):
    answer = []
    array = [[0]*n for _ in range(n)]
    pos = [[1, 0], [0, 1], [-1, -1]]
    num, x, y, cnt, idx = 1, -1, 0, 0, 0
    while n > 0:
        x += pos[idx][0]
        y += pos[idx][1]
        array[x][y] = num
        num += 1
        cnt += 1
        if cnt == n:
            cnt = 0
            n -= 1
            idx = (idx+1)%3
    for i in range(len(array)):
        for j in range(len(array)):
            if array[i][j] == 0:
                break
            answer.append(array[i][j])
    return answer