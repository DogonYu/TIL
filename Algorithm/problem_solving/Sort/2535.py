# 정렬 - 아시아 정보올림피아드

import sys

N = int(sys.stdin.readline())
info = sorted([list(map(str, sys.stdin.readline().strip().split(' '))) for _ in range(N)], key=lambda x: -int(x[2]))
mx = max([int(x[0]) for x in info])
answer = [0] * (mx + 1)
temp = 0

for x in info[:4]:
  answer[int(x[0])] += 1
  if answer[int(x[0])] < 3:
    print(x[0], x[1])
    temp += 1
  if temp == 3:
    break