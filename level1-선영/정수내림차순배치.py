def solution(n):
    num_list=[]
    
    while(n!=0):
        one_digit = n%10
        num_list.append(one_digit)
        n=n//10
    
    num_list.sort()
    num_list.reverse()
    print(num_list)
    n = 0
    #[int(i) for i in results]
    for i in num_list:
        n = n * 10 + int(i)
        
    return n
