# BFS - 토마토

import sys
from collections import deque

def dfs():
  answer = 1
  while queue:
    x, y = queue.popleft()
    for dx, dy in (0, 1), (0, -1), (1, 0), (-1, 0):
      nx, ny = x + dx, y + dy
      if 0 <= nx < M and 0 <= ny < N:
        if board[nx][ny] == 0:
          queue.append((nx, ny))
          board[nx][ny] = board[x][y] + 1
          answer = board[nx][ny]
  return answer

N, M = map(int, sys.stdin.readline().strip().split(' '))
board = [list(map(int, sys.stdin.readline().strip().split(' '))) for _ in range(M)]
queue = deque()

for i in range(M):
  for j in range(N):
    if board[i][j] == 1:
      queue.append((i, j))

result = dfs()
for i in range(M):
  for j in range(N):
    if board[i][j] == 0:
      print(-1)
      exit()
print(result-1)
