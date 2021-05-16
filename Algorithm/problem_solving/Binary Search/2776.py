# 이분탐색 - 암기왕

import sys

def bs(st, en, num):
  while st <= en:
    mid = (st + en) // 2
    if num == first[mid]:
      return 1
    elif num < first[mid]:
      en = mid - 1
    else:
      st = mid + 1
  return 0


T = int(sys.stdin.readline())

for _ in range(T):
  N = int(sys.stdin.readline())
  first = sorted(list(map(int, sys.stdin.readline().strip().split(' '))))
  M = int(sys.stdin.readline())
  second = list(map(int, sys.stdin.readline().strip().split(' ')))

  for x in second:
    print(bs(0, N-1, x))