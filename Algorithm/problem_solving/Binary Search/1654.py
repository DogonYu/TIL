# 이분탐색 - 랜선 자르기

import sys

K, N = map(int, sys.stdin.readline().strip().split(' '))
lans = sorted([int(sys.stdin.readline().strip()) for _ in range(K)])
st, en = 1, lans[-1]

while st <= en:
  mid = (st + en) // 2
  short_lan = 0

  for x in lans:
    short_lan += x // mid
  
  if short_lan >= N:
    st = mid + 1
  else:
    en = mid - 1

print(en)