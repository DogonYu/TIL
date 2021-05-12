# 그리디 - 알바생 강호

import sys

N = int(sys.stdin.readline())
M = sorted([int(sys.stdin.readline()) for _ in range(N)], key=lambda x: -x)
answer = []

for i in range(len(M)):
  tip = M[i] - ((i+1) - 1)
  if tip > -1:
    answer.append(tip)

print(sum(answer))