def solution(n,a,b):
    answer = 0
    arr = [x for x in range(1, n+1)]
    cnt = 0
    while True:
        cnt += 1
        new_arr = []
        for i in range(0, len(arr), 2):
            tmp = arr[i:i+2]
            if a in tmp and b in tmp:
                return cnt
            elif a in tmp:
                new_arr.append(a)
            elif b in tmp:
                new_arr.append(b)
            elif a not in tmp and b not in tmp:
                new_arr.append(tmp[0])
        arr = new_arr
    return answer

# 남의코드
# def solution(n,a,b):
#     answer = 0
#     while a != b:
#         answer += 1
#         a, b = (a+1)//2, (b+1)//2
#
#     return answer