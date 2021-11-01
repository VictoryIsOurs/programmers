def solution(arr):
    answer = []
    
    for i in range(len(arr)): ##이 부분 조심하기 !!  1,3,0,1 이므로, not in쓸수 X
        if i == 0:
            answer.append(arr[i])
            continue
        if arr[i] != arr[i-1]:
            answer.append(arr[i])
    return answer
  
 
