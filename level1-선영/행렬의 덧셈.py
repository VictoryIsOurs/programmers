def solution(arr1, arr2):
    
    for i in range(len(arr1)): # 총 길이:4
        for j in range(len(arr1[0])): # 0, 1
            arr1[i][j] += arr2[i][j]
    
    return arr1

#TypeError: 'list' object cannot be interpreted as an integer : 이중중첩 for문에서 len()을 안해줌.


#행렬 연산에서는 numpy를 뺼 수 없음. 
import numpy as np
def sumMatrix(A,B):
    A=np.array(A)
    B=np.array(B)
    answer=A+B
    return answer.tolist()

# 아래는 테스트로 출력해 보기 위한 코드입니다.
print(sumMatrix([[1,2], [2,3]], [[3,4],[5,6]]))
