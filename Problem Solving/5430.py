# 덱 - AC

import sys
from collections import deque

T = int(sys.stdin.readline())

for _ in range(T):
  p = sys.stdin.readline()[:-1]
  dcount = len([i for i in p if i == 'D'])
  n = int(sys.stdin.readline())
  x = deque(list(sys.stdin.readline()[1:-2].split(',')))
  reverse = False
  count = 0
  if '' in x:
    x = deque([])
  for i in range(len(p)):
    if len(x) == 0:
      break
    if p[i] == 'R':
      if reverse:
        reverse = False
      else:
        reverse = True
      count += 1
    if reverse and p[i] == 'D':
      x.pop()
    elif not reverse and p[i] == 'D':
      x.popleft()
  if dcount > n:
    print('error')
  else:
    if count % 2 != 0:
      x.reverse()
    print('[', end='')
    print(*x, sep=',', end=']\n')