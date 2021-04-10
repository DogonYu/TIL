import sys
from collections import deque

def dfs(graph, v, visited):
  for i in sorted(graph[v]):
    if i not in visited:
      visited.append(i)
      dfs(graph, i, visited)

def bfs(graph, start, visited):
  queue = deque([start])
  while queue:
    v = queue.popleft()
    for i in sorted(graph[v]):
      if i not in visited:
        queue.append(i)
        visited.append(i)

N, M, V = map(int, sys.stdin.readline().split(' '))
dfs_visited = [V]
bfs_visited = [V]
graph = {i+1:set() for i in range(N)}

for i in range(M):
  a, b = map(int, sys.stdin.readline().split(' '))
  graph[a].add(b)
  graph[b].add(a)

dfs(graph, V, dfs_visited)
for i in range(len(dfs_visited)):
  if len(dfs_visited)-1 != i:
    print(dfs_visited[i], end=' ')
  else:
    print(dfs_visited[i])
bfs(graph, V, bfs_visited)
for i in range(len(bfs_visited)):
  if len(bfs_visited)-1 != i:
    print(bfs_visited[i], end=' ')
  else:
    print(bfs_visited[i])