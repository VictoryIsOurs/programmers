def solution(numbers):
    answer = []
    for num in numbers:
        b_num = list('0' + bin(num)[2:])
        idx = ''.join(b_num).rfind('0')
        b_num[idx] = '1'
        if num % 2 != 0:
            b_num[idx+1] = '0'
        answer.append(int(''.join(b_num), 2))
    return answer