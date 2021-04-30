# BFS - 토마토

import sys
from collections import deque

def bfs():
  while queue:
    z, x, y = queue.popleft()
    for dz, dx, dy in (1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1):
      nz, nx, ny = z + dz, x + dx, y + dy
      if 0 <= nz < H and 0 <= nx < M and 0 <= ny < N:
        if board[nz][nx][ny] == 0:
          queue.append((nz, nx, ny))
          board[nz][nx][ny] = board[z][x][y] + 1
  return board[z][x][y] - 1

N, M, H = map(int, sys.stdin.readline().strip().split(' '))
board = []
queue = deque()

for _ in range(H):
  temp = [list(map(int, sys.stdin.readline().strip().split(' '))) for _ in range(M)]
  board.append(temp)

for i in range(H):
  for j in range(M):
    for k in range(N):
      if board[i][j][k] == 1:
        queue.append((i, j, k))

result = bfs()
for i in range(H):
  for j in range(M):
    for k in range(N):
      if board[i][j][k] == 0:
        print(-1)
        exit()
print(result)