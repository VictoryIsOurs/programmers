def binary(n):
    cnt = 0
    while n:
        rem = n % 2
        if rem == 1:
            cnt += 1
        n //= 2
    return cnt

def solution(n):
    n_cnt = binary(n)
    while True:
        n += 1
        next_n_cnt = binary(n)
        if next_n_cnt == n_cnt:
            break
    return n