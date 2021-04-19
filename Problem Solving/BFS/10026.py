# BFS - 적록색약

import sys
from collections import deque

def normal_bfs(color, i, j):
  queue1.append((i, j))
  visited1[i][j] = 1
  while queue1:
    x, y = queue1.popleft()
    for dx, dy in (0, 1), (0, -1), (1, 0), (-1, 0):
      nx, ny = x + dx, y + dy
      if 0 <= nx < N and 0 <= ny < N:
        if visited1[nx][ny] == 0 and board[nx][ny] == color:
          queue1.append((nx, ny))
          visited1[nx][ny] = 1

def special_bfs(color, i, j):
  queue2.append((i, j))
  visited2[i][j] = 1
  while queue2:
    x, y = queue2.popleft()
    for dx, dy in (0, 1), (0, -1), (1, 0), (-1, 0):
      nx, ny = x + dx, y + dy
      if 0 <= nx < N and 0 <= ny < N:
        if visited2[nx][ny] == 0 and (board[nx][ny] == color[0] or board[nx][ny] == color[1]):
          queue2.append((nx, ny))
          visited2[nx][ny] = 1

N = int(sys.stdin.readline())
board = [list(sys.stdin.readline().strip()) for _ in range(N)]
queue1 = deque()
queue2 = deque()
visited1 = [[0] * N for _ in range(N)]
visited2 = [[0] * N for _ in range(N)]
answer1 = 0
answer2 = 0

for i in range(N):
  for j in range(N):
    if visited1[i][j] == 0:
      if board[i][j] == 'R':
        normal_bfs('R', i, j)
        answer1 += 1
      if board[i][j] == 'G':
        normal_bfs('G', i, j)
        answer1 += 1
      if board[i][j] == 'B':
        normal_bfs('B', i, j)
        answer1 += 1

for i in range(N):
  for j in range(N):
    if visited2[i][j] == 0:
      if board[i][j] == 'R' or board[i][j] == 'G':
        special_bfs('RG', i, j)
        answer2 += 1
      elif board[i][j] == 'B':
        special_bfs('BZ', i, j)
        answer2 += 1

print(answer1, answer2)