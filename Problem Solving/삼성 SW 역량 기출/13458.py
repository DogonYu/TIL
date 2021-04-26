# 시험 감독

import sys

N = int(sys.stdin.readline())
A = list(map(int, sys.stdin.readline().strip().split(' ')))
B, C = map(int, sys.stdin.readline().strip().split(' '))
answer = 0

for i in A:
  answer += 1
  if i - B < 0:
    temp = 0
  elif i - B >= 0:
    temp = i - B
  if temp / C > int(temp / C):
    answer += temp // C + 1
  elif temp / C == int(temp / C):
    answer += temp // C

print(answer)