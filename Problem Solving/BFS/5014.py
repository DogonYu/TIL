# BFS - 스타트링크

import sys
from collections import deque

def bfs():
  while queue:
    x, count = queue.popleft()
    if x + U <= F:
      if x + U == G:
        return count + 1
      if visited[x + U] == 0:
        queue.append((x + U, count + 1))
        visited[x + U] = 1
    if 0 < x - D <= F:
      if x - D == G:
        return count + 1
      if visited[x - D] == 0:
        queue.append((x - D, count + 1))
        visited[x - D] = 1
  return 'use the stairs'

F, S, G, U, D = map(int, sys.stdin.readline().strip().split(' '))
visited = [0 for _ in range(F+1)]
queue = deque([(S, 0)])
visited[S] = 1
if S == G:
  print(0)
else:
  result = bfs()
  print(result)