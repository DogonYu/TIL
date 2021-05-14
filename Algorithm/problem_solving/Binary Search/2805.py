# 이분탐색 - 나무 자르기

import sys

N, M = map(int, sys.stdin.readline().strip().split(' '))
trees = sorted(list(map(int, sys.stdin.readline().strip().split(' '))))
st, en = 1, trees[-1]

while st <= en:
  mid = (st + en) // 2
  felled_tree = sum([x - mid if x >= mid else 0 for x in trees])
  
  if felled_tree >= M:
    st = mid + 1
  else:
    en = mid - 1

print(en)