# BFS - 아기 상어2

import sys
from collections import deque

def bfs():
  while queue:
    y, x = queue.popleft()
    for dx, dy in (0,1),(0,-1),(1,0),(-1,0),(1,1),(-1,-1),(1,-1),(-1,1):
      ny, nx = y+dy, x+dx
      if 0 <= ny < N and 0 <= nx < M:
        if not board[ny][nx]:
          board[ny][nx] = board[y][x]+1
          queue.append([ny,nx])

N, M = map(int, sys.stdin.readline().split(' '))
board = [list(map(int, sys.stdin.readline()[:-1].split(' '))) for _ in range(N)]
queue = deque()

for i in range(N):
  for j in range(M):
    if board[i][j] == 1:
      queue.append((i,j))
bfs()
print(max(map(max, board))-1)