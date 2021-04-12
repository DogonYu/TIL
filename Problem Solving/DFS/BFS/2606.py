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

N = int(sys.stdin.readline())
K = int(sys.stdin.readline())
graph = {i+1:set() for i in range(N)}

for i in range(K):
  a, b = map(int, sys.stdin.readline().split(' '))
  graph[a].add(b)
  graph[b].add(a)

visited = []
bfs(graph, 1, visited)
print(len(visited)-1)