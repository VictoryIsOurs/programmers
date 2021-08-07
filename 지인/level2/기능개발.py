import math

def solution(prog, speeds):
    answer = []
    check = [False] * len(prog)
    arr = []
    for i in range(len(prog)):
        arr.append(math.ceil((100-prog[i])/speeds[i]))
    for i in range(len(arr)):
        if not check[i]:
            cnt = 1
            check[i] = True
            for j in range(i+1, len(arr)):
                if arr[i] < arr[j]:
                    break
                check[j] = True
                cnt += 1
            answer.append(cnt)

    return answer
