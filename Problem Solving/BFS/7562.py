# BFS - 나이트의 이동

import sys
from collections import deque

def bfs(i, j):
  queue = deque()
  queue.append((i, j))
  visited[i][j] = 1
  while queue:
    x, y = queue.popleft()
    for dx, dy in (1, 2), (1, -2), (-1, 2), (-1, -2), (2, 1), (2, -1), (-2, 1), (-2, -1):
      nx, ny = x + dx, y + dy
      if [nx, ny] == _next:
        return board[x][y] + 1
      if 0 <= nx < N and 0 <= ny < N:
        if visited[nx][ny] == 0:
          queue.append((nx, ny))
          visited[nx][ny] = 1
          board[nx][ny] = board[x][y] + 1


T = int(sys.stdin.readline())

for _ in range(T):
  N = int(sys.stdin.readline())
  board = [[0] * N for _ in range(N)]
  visited = [[0] * N for _ in range(N)]
  current_x, current_y = map(int, sys.stdin.readline().strip().split(' '))
  _next = list(map(int, sys.stdin.readline().strip().split(' ')))
  if [current_x, current_y] != _next:
    result = bfs(current_x, current_y)
  else:
    result = 0
  print(result)