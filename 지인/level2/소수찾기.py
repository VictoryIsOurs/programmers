import itertools

MAX = 10000000
p = [1] * MAX
p[0], p[1] = 0, 0

def is_prime():
    for i in range(2, MAX):
        if p[i] == 1:
            for j in range(i + i, MAX, i):
                p[j] = 0

def solution(numbers):
    total_set = set()
    for r in range(1, len(numbers) + 1):
        permu_list = list(map(''.join, itertools.permutations(numbers, r)))
        permu_list = list(map(int, permu_list))
        total_set.update(permu_list)
    total_set = list(total_set)

    is_prime()

    cnt = 0
    for n in total_set:
        if p[n] == 1:
            cnt += 1
    return cnt