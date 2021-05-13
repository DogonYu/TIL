# 이분탐색 - 수 찾기

import sys

N = int(sys.stdin.readline())
A = sorted(list(map(int, sys.stdin.readline().strip().split(' '))))
M = int(sys.stdin.readline())
B = list(map(int, sys.stdin.readline().strip().split(' ')))

for x in B:
  st, en = 0, len(A) - 1
  while st <= en:
    mid = (en + st) // 2
    # print(x, A[mid])
    if x == A[mid]:
      print(1)
      break
    elif x < A[mid]:
      en = mid - 1
    elif x > A[mid]:
      st = mid + 1
  else:
    print(0)
