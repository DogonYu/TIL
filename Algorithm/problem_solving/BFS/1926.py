# BFS - 그림

import sys
from collections import deque

def bfs(x, y):
  queue = deque([(x, y)])
  board[x][y] = 0
  answer = 1
  while queue:
    x, y = queue.popleft()
    for nx, ny in (0, 1), (0, -1), (1, 0), (-1, 0):
      dx, dy = x + nx, y + ny
      if 0 <= dx < N and 0 <= dy < M:
        if board[dx][dy] == 1:
          queue.append((dx, dy))
          board[dx][dy] = 0
          answer += 1
  result.append(answer)

N, M = map(int, sys.stdin.readline().split(' '))
board = [list(map(int, sys.stdin.readline().strip().split(' '))) for _ in range(N)]
result = []
count = 0

for i in range(N):
  for j in range(M):
    if board[i][j] == 1:
      bfs(i, j)
      count += 1

print(count)
if result:
  print(max(result))
else:
  print(0)