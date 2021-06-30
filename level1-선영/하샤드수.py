def solution(n):
    
    original_num = n
    num_sum = 0
    
    for k in range(5): #제한 조건에서 x는 1이상, 10000이하인 정수라고 했으므로, 최대 5자리까지 가능
        i = n % 10 #제일 끝 자리 떼어주기
        num_sum += i #각자리수 더해줌.
        try:
            n = n//10 #n에서 제일 끝자리 숫자 떼어주기
        except ZeroDivisionError:
            break
            
    
    if(original_num % num_sum == 0):
        return True
    else:
        return False
     
    
    

# 최적화된 코드
def Harshad(n):
    # n은 하샤드 수 인가요?
    return n % sum([int(c) for c in str(n)]) == 0

# 아래는 테스트로 출력해 보기 위한 코드입니다.
print(Harshad(18))


#다른 코드
def Harshad(n):
    # n은 하샤드 수 인가요?
    st = str(n)
    a = 0
    for i in range(len(st)):
        a += int(st[i])

    return True if n%a == 0 else False

# 아래는 테스트로 출력해 보기 위한 코드입니다.
print(Harshad(18))
