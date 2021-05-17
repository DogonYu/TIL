# 구현 - 날짜 계산

import sys

E, S, M = map(int, sys.stdin.readline().strip().split(' '))
earth, sun, moon = 1, 1, 1
answer = 1

while True:
  if earth == E and sun == S and moon == M:
    break
  earth += 1
  sun += 1
  moon += 1
  if earth > 15:
    earth = 1
  if sun > 28:
    sun = 1
  if moon > 19:
    moon = 1
  answer += 1

print(answer)