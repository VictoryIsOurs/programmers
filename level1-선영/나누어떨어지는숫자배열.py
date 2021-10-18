num_list = []

def solution(arr, divisor):
    
    for i in arr:
        n = i%divisor
        if n == 0: #나누어 떨어지면
             num_list.append(i) #제일 끝에 추가

    num_list.sort() #리스트 정렬

    if len(num_list) == 0:
        return [-1]
    
    return num_list
