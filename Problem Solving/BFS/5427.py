# BFS - 불

import sys
from collections import deque

def fire_bfs():
  while queue1:
    x, y = queue1.popleft()
    for dx, dy in (0, 1), (0, -1), (1, 0), (-1, 0):
      nx, ny = x + dx, y + dy
      if 0 <= nx < M and 0 <= ny < N:
        if fire[nx][ny] == -1 and maze[nx][ny] != '#':
          queue1.append((nx, ny))
          fire[nx][ny] = fire[x][y] + 1

def escape_bfs():
  while queue2:
    x, y = queue2.popleft()
    for dx, dy in (0, 1), (0, -1), (1, 0), (-1, 0):
      nx, ny = x + dx, y + dy
      if 0 <= nx < M and 0 <= ny < N:
        if escape[nx][ny] == -1 and maze[nx][ny] != '#' and (fire[nx][ny] == -1 or escape[x][y] + 1 < fire[nx][ny]):
          queue2.append((nx, ny))
          escape[nx][ny] = escape[x][y] + 1
      else:
        print(escape[x][y] + 1)
        return
  print('IMPOSSIBLE')

T = int(sys.stdin.readline())

for _ in range(T):
  N, M = map(int, sys.stdin.readline().strip().split(' '))
  maze = [list(sys.stdin.readline().strip()) for _ in range(M)]
  queue1 = deque()
  queue2 = deque()
  fire = [[-1] * N for _ in range(M)]
  escape = [[-1] * N for _ in range(M)]

  for i in range(M):
    for j in range(N):
      if maze[i][j] == '*':
        fire[i][j] = 0
        queue1.append((i, j))
      if maze[i][j] == '@':
        escape[i][j] = 0
        queue2.append((i, j))

  fire_bfs()
  escape_bfs()