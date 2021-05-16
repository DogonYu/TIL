# 이분탐색 - 게임

import sys

X, Y = map(int, sys.stdin.readline().strip().split(' '))
Z = Y * 100 / X
answer = 0

if Z >= 99:
  print(-1)
else:
  st, en = 1, 1000000000
  while st <= en:
    mid = (st + en) // 2
    tx, ty = X + mid, Y + mid
    
    if ty * 100 // tx <= Z:
      st = mid + 1
    else:
      answer = mid
      en = mid - 1

  print(answer)