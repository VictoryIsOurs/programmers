def solution(numbers):

    answer = []
    
    for i in range(len(numbers)): ##range값 잘 보기
        for j in range(i+1, len(numbers)):##range값 잘 보기
            sum = numbers[i] + numbers[j]

            if sum not in answer:
                answer.append(sum)
            
    answer.sort()
    return answer
