DAY = ['THU','FRI','SAT','SUN','MON','TUE','WED']
#2016.01.01은 FRI - 7로 나눴을 때, 나머지가 1이면 FRI로 설정

#2016년은 윤년이라서 2월 29일 까지 있다!
DAY_COUNT = [31, 29, 31, 30, 31, 30 ,31,31,30, 31,30,31] 

def solution(a, b):
    day = 0 
    
    if a == 1: #1월은 31일을 다 못채웠기 때문에 따로 예외처리
        day = day + b
        
    else:
        for i in range(0,a-1): #달 계산 #a-1은 그 전달까지만 다 더해줘야해서
            day = day + DAY_COUNT[i] #그 전달까지 더해줌.       
        day = day + b #일 계산
    
    #WhatDay = day%7
    
    return DAY[day%7]
    
