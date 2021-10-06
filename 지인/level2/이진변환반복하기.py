def binary(n):
    a = ''
    while n > 0:
        a += str(n%2)
        n //= 2
    return a[::-1]

def solution(ss):
    cnt, step = 0, 0

    while ss != '1':
        step += 1
        del_zero = ''
        for s in ss:
            if s == '1':
                del_zero += s
        cnt += len(ss) - len(del_zero)
        ss = binary(len(del_zero))

    return [step, cnt]

# 남의 풀이
# 파이썬은 10진법을 2진법으로 바로 바꿔주는 bin 이라는 함수가 있다.
# 또한 문자열에서 해당 문자열의 개수를 세어주는 count 라는 함수도 있다.
# 사실 나도 문제 푸는데 오래 걸리진 않았지만, 그래도 더 쉽고 간단한 방법이 있다는 것은 알아놓자.
# 풀기 전에 사용할 수 있는 라이브러리가 뭐가 있는지 5초만 생각하고 풀이 생각하기

# def solution(s):
#     a, b = 0, 0
#     while s != '1':
#         a += 1
#         num = s.count('1')
#         b += len(s) - num
#         s = bin(num)[2:]
#     return [a, b]