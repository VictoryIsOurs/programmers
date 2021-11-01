def solution(s):
    
    if s.count('p')+s.count('P') == s.count('y')+s.count('Y'):
        return True
    else : 
        return False
      
    ## list로 굳이 바꾸지 말고, count함수를 써서 그 안의 문자를 세주자.
