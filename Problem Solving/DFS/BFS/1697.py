import sys
from collections import deque

def bfs(graph, start, visited):
  queue = deque([start])
  while queue:
    v = queue.popleft()
    for i in graph[v]:
      if i not in visited:
        queue.append(i)
        visited.append(i)

N, K = map(int, sys.stdin.readline().split(' '))

