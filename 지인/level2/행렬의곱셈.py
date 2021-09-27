def solution(arr1, arr2):
    answer = []
    convert_arr2 = []
    for i in range(len(arr2[0])):
        tmp = []
        for j in range(len(arr2)):
            tmp.append(arr2[j][i])
        convert_arr2.append(tmp)
    for a1 in arr1:
        tmp = []
        for a2 in convert_arr2:
            res = 0
            for i in range(len(a1)):
                res += a1[i] * a2[i]
            tmp.append(res)
        answer.append(tmp)
    return answer

# 남의코드
# def productMatrix(A, B):
#     return [[sum(a*b for a, b in zip(A_row,B_col)) for B_col in zip(*B)] for A_row in A]
# zip(*B)는 내가 만든 함수인 convert_arr2와 동일한 역할을 한다