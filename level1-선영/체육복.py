def solution(n, lost, reserve): #lost도난 #reverse여벌옷 있는 애들
    answer = 0
    count_num = n - len(lost) #!!!!!!!!!!!!!!중요!!!!!!! 
    possible_num = []
    
    for i in reserve: #[1,3,5]
        for j in lost: #[2,4]
            if i-1 == j:
                possible_num.append(i)
                count_num +=1
                continue
            elif i+1 == j:
                possible_num.append(j)
                count_num +=1
                continue
                
    print(possible_num)
    
            
    return count_num

  
  #다시 풀기!!!!!!!
