#계속 index오류가 남. for문안에서 del을 해줘서 그럼.
#문제점 : str을 자꾸 list로 받아서 하려고 함. str은 str로 받자 제발!

def solution(new_id):
    
    #1단계
    new_id = new_id.lower()
#    for i in range(len_new_id):
#        if(new_id[i].isupper() == True): #1단계
#                new_id[i].lower()
    
    #2단계
    answer = ''
    for i in new_id:
        if i.islower() or i.isdigit() or i in '-_.': #오답났던 부분
            answer += i
    
    #3단계
    while '..' in answer:
            answer = answer.replace("..", ".")
            
    #4단계                
    if(answer[0] == '.' and len(answer)>1): #오답 : & 이라고 씀.
            answer = answer[1:]
            
    if answer[-1] == '.': #오답: answer[len(answer)] == '.'
            answer = answer[:-1]
    
    #5단계
    if len(answer)==0:
        answer = 'a'
        
    #6단계
    if len(answer)>=16:
        answer = answer[:15]
        if(answer[-1]) == '.':
            answer = answer[:-1]
            
    #7단계
    if len(answer) <= 3:
        answer = answer + answer[-1]*(3-len(answer))
    
    return answer


#참고 사이트  : https://greendreamtrre.tistory.com/22 for문안에서 list del쓰면 ㄴㄴ


#최적화된 코드 

#정규식
import re

def solution(new_id):
    st = new_id
    st = st.lower()
    st = re.sub('[^a-z0-9\-_.]', '', st)
    st = re.sub('\.+', '.', st)
    st = re.sub('^[.]|[.]$', '', st)
    st = 'a' if len(st) == 0 else st[:15]
    st = re.sub('^[.]|[.]$', '', st)
    st = st if len(st) > 2 else st + "".join([st[-1] for i in range(3-len(st))])
    return st
