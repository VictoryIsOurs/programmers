def solution(phone_number):
    #전제 문자열 길이 구하기 
    len_phoneNumber = len(phone_number)
    
    #맨 뒤 4자리를 제외한 자리만크 *붙이기
    star_str = ""
    for i in range(len_phoneNumber -4):
        star_str += "*"
        
    return star_str + phone_number[-4::]



#최적화된 코드
def hide_numbers(s):
    return "*"(len(s)-4) + s[-4::]
