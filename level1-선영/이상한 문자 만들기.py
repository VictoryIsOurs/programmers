def solution(s):
    word_list = s.split(' ') #여기서 공백으로 나눠줌. 
    new_word=""
    
    for word in word_list:
        for i in range(len(word)):
            if i%2==0:
                new_word += word[i].upper() #짝수 번째는 대문자
            else: 
                new_word += word[i].lower() #홀수는 소문자
        new_word += ' '
        
    if new_word[-1] == ' ':
        new_word = new_word[:-1]
    return new_word
