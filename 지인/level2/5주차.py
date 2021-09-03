# 위클리 챌린지 5주차 문제
from itertools import product
def solution(word):
    answer = []
    alphabet = "AEIOU"
    for r in range(1, 6):
        answer += list(map(''.join, product(alphabet, repeat=r)))
    answer.sort()
    for i in range(len(answer)):
        if answer[i] == word:
            return i+1