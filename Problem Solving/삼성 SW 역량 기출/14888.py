# 연산자 끼워넣기

import sys
from itertools import permutations

N = int(sys.stdin.readline())
A = list(map(int, sys.stdin.readline().strip().split(' ')))
add, sub, mul, div = map(int, sys.stdin.readline().strip().split(' '))
operators = ['+'] * add + ['-'] * sub + ['*'] * mul + ['/'] * div
operators = set(permutations(operators))
answer = []

for op in operators:
  result = A[0]
  for i in range(N-1):
    if op[i] == '/':
      result = int(result / A[i+1])
    elif op[i] == '+':
      result = result + A[i+1]
    elif op[i] == '*':
      result = result * A[i+1]
    elif op[i] == '-':
      result = result - A[i+1]
  answer.append(result)

print(max(answer))
print(min(answer))