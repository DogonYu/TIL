# 이분탐색 - 숫자 카드

import sys

N = int(sys.stdin.readline())
A = sorted(list(map(int, sys.stdin.readline().strip().split(' '))))
M = int(sys.stdin.readline())
B = list(map(int, sys.stdin.readline().strip().split(' ')))
dict = {}
# dict = {x:0 for x in B}

# for x in A:
#   try:dict[x] += 1
#   except:dict[x] = 0

# print(' '.join(map(str, [dict[x] for x in B])))

for x in A:
  st, en = 0, len(A) - 1
  if x not in dict:
    while st <= en:
      mid = (en + st) // 2
      if x == A[mid]:
        dict[x] = A[st:en+1].count(x)
        break
      elif x < A[mid]:
        en = mid - 1
      else:
        st = mid + 1
    else:
      dict[x] = 0

print(' '.join(map(str, [dict[x] if x in dict else '0' for x in B])))