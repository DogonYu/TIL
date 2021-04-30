# BFS - A -> B

import sys
from collections import deque

A, B = map(int, sys.stdin.readline().split(' '))
answer = -1
queue = deque([(A, 1)])
visited = []

while queue:
  v, cnt = queue.popleft()
  if v == B:
    answer = cnt
    break
  if v*2 <= B:
    queue.append((v*2, cnt+1))
  if int(str(v)+'1') <= B:
    queue.append((int(str(v)+'1'), cnt+1))

print(answer)