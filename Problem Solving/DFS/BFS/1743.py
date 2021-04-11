import sys
from collections import deque

def bfs(graph, start, visited):
  count = 0
  queue = deque([start])
  if graph[start[0]][start[1]] == 1:
    visited.append(start)
    count += 1
  while queue:
    v = queue.popleft()
    for dx, dy in (1, 0), (-1, 0), (0, -1), (0, 1):
      nx, ny = v[0]+dx, v[1]+dy
      if 0 <= nx < N and 0 <= ny < M:
        if [nx, ny] not in visited and garbage[nx][ny] == 1:
          queue.append([nx, ny])
          visited.append([nx, ny])
          count += 1
  return [visited, count]

N, M, K = map(int, sys.stdin.readline().split(' '))
visited = []
count = 0
garbage = [[0 for _ in range(M)] for _ in range(N)]

for _ in range(K):
  r, c = map(int, sys.stdin.readline().split(' '))
  garbage[r-1][c-1] = 1

size = 0
for i in range(N):
  for j in range(M):
    if [i, j] not in visited and garbage[i][j] == 1:
      visited, compare_size = bfs(garbage, [i, j], visited)
      if size < compare_size:
        size = compare_size

print(size)