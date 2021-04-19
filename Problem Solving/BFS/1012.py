# BFS - 유기농 배추

import sys
from collections import deque

def bfs(i, j):
  queue = deque()
  queue.append((i, j))
  while queue:
    x, y = queue.popleft()
    for dx, dy in (0, 1), (0, -1), (1, 0), (-1, 0):
      nx, ny = x + dx, y + dy
      if 0 <= nx < M and 0 <= ny < N:
        if board[nx][ny] == 1:
          queue.append((nx, ny))
          board[nx][ny] = 0
  board[x][y] = 0

T = int(sys.stdin.readline())

for _ in range(T):
  N, M, K = map(int, sys.stdin.readline().strip().split(' '))
  board = [[0] * N for _ in range(M)]
  answer = 0

  for _ in range(K):
    y, x = map(int, sys.stdin.readline().strip().split(' '))
    board[x][y] = 1
  
  for i in range(M):
    for j in range(N):
      if board[i][j] == 1:
        board[i][j] = 0
        bfs(i, j)
        answer += 1

  print(answer)