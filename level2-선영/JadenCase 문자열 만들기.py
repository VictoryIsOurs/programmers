def solution(s):
    answer = ''
    string_list = s.split(' ') #공백으로 나눠준다.
    
    for word in string_list:
        word = word.lower()
        word = word.capitalize() #이렇게 간단하게 풀자
        #word = word[0].upper()+word[1::].lower() #런타임 오류
        #(오답) 여기서 그냥 lower()만 해주면 안되고 꼭 할당을 해줘야함!!!!!!!!
        
        answer = answer + word
        answer+=' '
        
    
    answer = answer[:len(answer)-1:] #마지막 빈칸은 없애주기
    
    return answer
