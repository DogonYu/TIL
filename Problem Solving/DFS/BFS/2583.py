# BFS - 영역 구하기

import sys
from collections import deque

def bfs(i, j):
  area = 1
  queue = deque()
  queue.append((i, j))
  board[i][j] = 1
  while queue:
    x, y = queue.popleft()
    for dx, dy in (0, 1), (0, -1), (1, 0), (-1, 0):
      nx, ny = x + dx, y + dy
      if 0 <= nx < M and 0 <= ny < N:
        if board[nx][ny] == 0:
          queue.append((nx, ny))
          board[nx][ny] = 1
          area += 1
  board[x][y] = 1
  return area

M, N, K = map(int, sys.stdin.readline().strip().split(' '))
board = [[0] * N for _ in range(M)]
result = []
count = 0

for _ in range(K):
  x1, y1, x2, y2 = map(int, sys.stdin.readline().strip().split(' '))
  for i in range(y1, y2):
    for j in range(x1, x2):
      board[i][j] = 1

for i in range(M):
  for j in range(N):
    if board[i][j] != 1:
      result.append(bfs(i, j))
      count += 1

print(count)
print(*sorted(result))