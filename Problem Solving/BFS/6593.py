# BFS - 상범 빌딩

import sys
from collections import deque

def bfs():
  while queue:
    z, x, y = queue.popleft()
    for dz, dx, dy in (1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1):
      nz, nx, ny = z + dz, x + dx, y + dy
      if 0 <= nz < T and 0 <= nx < N and 0 <= ny < M:
        if visited[nz][nx][ny] == 0:
          if board[nz][nx][ny] == '.':
            queue.append((nz, nx, ny))
            visited[nz][nx][ny] = visited[z][x][y] + 1
          if board[nz][nx][ny] == 'E':
            visited[nz][nx][ny] = visited[z][x][y] + 1
            return f'Escaped in {visited[nz][nx][ny]} minute(s).'
  return 'Trapped!'
          

while True:
  T, N, M = map(int, sys.stdin.readline().split(' '))
  queue = deque()
  board = []
  visited = []

  if [T, N, M] == [0, 0, 0]:
    exit()

  for _ in range(T):
    temp1 = [list(sys.stdin.readline().strip()) for _ in range(N)]
    temp2 = [[0] * M for _ in range(N)]
    sys.stdin.readline()
    board.append(temp1)
    visited.append(temp2)

  for i in range(T):
    for j in range(N):
      for k in range(M):
        if board[i][j][k] == 'S':
          queue.append((i, j, k))
  print(bfs())