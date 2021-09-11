# 내 풀이 -> 너무 정석인가...
from itertools import permutations
import math

def solution(expression):
    lst = []
    tmp = ''
    for exp in expression:
        if exp == '-' or exp == '*' or exp == '+':
            lst.append(int(tmp))
            lst.append(exp)
            tmp = ''
        else:
            tmp += exp
    lst.append(int(tmp))

    postfix, op = [], []
    pool = ['*', '+', '-']
    permu = list(permutations(pool))
    MAX = -math.inf
    for p in permu:
        # 후위표기식으로 변환
        priority = {}
        priority[p[0]], priority[p[1]], priority[p[2]] = 1, 2, 3
        for l in lst:
            if l != '-' and l != '*' and l != '+':
                postfix.append(l)
            else:
                if not op:
                    op.append(l)
                else:
                    if priority[op[-1]] <= priority[l]:
                        while op and priority[op[-1]] <= priority[l]:
                            postfix.append(op.pop())
                        op.append(l)
                    else:
                        op.append(l)
        while op:
            postfix.append(op.pop())
        # 후위표기식 계산
        operand = []
        for p in postfix:
            if p == '*':
                operand.append(operand.pop() * operand.pop())
            elif p == '+':
                operand.append(operand.pop() + operand.pop())
            elif p == '-':
                fst = operand.pop()
                snd = operand.pop()
                operand.append(snd - fst)
            else:
                operand.append(p)
        MAX = max(MAX, abs(operand[-1]))

    return MAX

# 남의 풀이
# def solution(expression):
#     operations = [('+', '-', '*'),('+', '*', '-'),('-', '+', '*'),('-', '*', '+'),('*', '+', '-'),('*', '-', '+')]
#     answer = []
#     for op in operations:
#         a = op[0]
#         b = op[1]
#         temp_list = []
#         for e in expression.split(a):
#             temp = [f"({i})" for i in e.split(b)]
#             temp_list.append(f'({b.join(temp)})')
#         answer.append(abs(eval(a.join(temp_list))))
#     return max(answer)