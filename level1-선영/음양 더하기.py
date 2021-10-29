def solution(absolutes, signs):
    sum = 0
    for i in range(len(absolutes)):        
        if signs[i] == True:
            sum += absolutes[i]
        elif signs[i] == False:
            sum -= absolutes[i]
    return sum
  
  #이거는 True, False를 배열에 "true", "false"로 들어있길래 그렇게 썼다가 계속 틀림.. 다시 풀 필요는 없을듯
