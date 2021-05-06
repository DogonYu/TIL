# BFS - 연결 요소의 개수

import sys
from collections import deque

def bfs(x, answer):
  queue.append(x)
  visited.append(x)
  while queue:
    v = queue.popleft()
    for e in graph[v]:
      if e not in visited:
        queue.append(e)
        visited.append(e)
  return 1

N, M = map(int, sys.stdin.readline().strip().split(' '))
nums = [list(map(int, sys.stdin.readline().strip().split(' '))) for _ in range(M)]
graph = {i:set() for i in range(1, N+1)}
visited = []
queue = deque()
answer = 0

for u,v in nums:
  graph[u].add(v)
  graph[v].add(u)

for i in range(1, N+1):
  if i not in visited:
    answer += bfs(i, answer)

print(answer)