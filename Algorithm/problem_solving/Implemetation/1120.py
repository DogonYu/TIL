# 구현 - 문자열

import sys

N = int(sys.stdin.readline())

for _ in range(N):
  A, B = map(str, sys.stdin.readline().strip().split(' '))
  x = sorted(list(A))
  y = sorted(list(B))

  if x == y:
    print(f'{A} & {B} are anagrams.')
  else:
    print(f'{A} & {B} are NOT anagrams.')