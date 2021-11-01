def gcd(a, b):
    return gcd(b, a % b) if b else a

def lcm(a, b):
    return a * b // gcd(a, b)

def solution(arr):
    ans = arr[0]
    for i in range(1, len(arr)):
        ans = lcm(ans, arr[i])
    return ans