def solution(answers):
    stu1 = [1,2,3,4,5]
    stu2 = [2,1,2,3,2,4,2,5]
    stu3 = [3,3,1,1,2,2,4,4,5,5]
    score1, score2, score3 = 0,0,0
    
    for i in range(len(answers)):
        count1 = i%len(stu1) #index값을 나타냄
        count2 = i%len(stu2)
        count3 = i%len(stu3)
        
        if stu1[count1] == answers[i]:
            score1+=1
        if stu2[count2] == answers[i]:
            score2+=1
        if stu3[count3] == answers[i]:
            score3+=1
        
    max_score = max(score1, score2, score3)
    
    answer = []
    if max_score == score1:
        answer.append(1)
    if max_score == score2:
        answer.append(2)
    if max_score == score3:
        answer.append(3)
        
    return answer
