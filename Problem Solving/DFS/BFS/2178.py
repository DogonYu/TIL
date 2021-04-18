# BFS - 미로 탐색

import sys
from collections import deque

def bfs(x, y, visited):
  queue = deque([[x, y]])
  visited[x][y] = 1
  while queue:
    v = queue.popleft()
    for dx, dy in (1, 0), (-1, 0), (0, 1), (0, -1):
      nx, ny = v[0]+dx, v[1]+dy
      if 0 <= nx < N and 0 <= ny < M:
        if maze[nx][ny] == '1' and visited[nx][ny] == 0:
          visited[nx][ny] = visited[v[0]][v[1]] + 1
          queue.append([nx, ny])
  return visited[-1][-1]

maze = []
count = 0
N, M = map(int, sys.stdin.readline().split(' '))
visited = [[0 for _ in range(M)] for _ in range(N)]
for _ in range(N):
  maze.append(sys.stdin.readline()[:M])

print(bfs(0, 0, visited))