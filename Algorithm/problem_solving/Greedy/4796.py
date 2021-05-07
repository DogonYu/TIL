# 그리디 - 캠핑

import sys

i = 1
while True:
  answer = 0
  L, P, V = map(int, sys.stdin.readline().strip().split(' '))
  if [0 ,0 ,0] == [L, P, V]: break

  div, mod = divmod(V, P)
  if div:
    answer += L * div
  if mod and L <= mod:
    answer += L
  else:
    answer += mod

  print(f'Case {i}: {answer}')
  i += 1