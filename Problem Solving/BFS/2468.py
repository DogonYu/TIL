# BFS - 안전 영역

import sys
from collections import deque

def bfs(H):
  while queue:
    x, y = queue.popleft()
    for dx, dy in (0, 1), (0, -1), (1, 0), (-1, 0):
      nx, ny = x + dx, y + dy
      if 0 <= nx < N and 0 <= ny < N:
        if flooding_board[H][nx][ny] > H and visited[nx][ny] == 0:
          queue.append((nx, ny))
          visited[nx][ny] = 1

N = int(sys.stdin.readline())
board = [list(map(int, sys.stdin.readline().strip().split(' '))) for _ in range(N)]
flooding_board = []
result = []
H = max([y for x in board for y in x]) + 1

for i in range(H):
  temp2 = []
  for j in range(N):
    temp1 = []
    for k in range(N):
      if board[j][k] <= i:
        temp1.append(-1)
      else:
        temp1.append(board[j][k])
    temp2.append(temp1)
  flooding_board.append(temp2)

for i in range(H-1):
  queue = deque()
  visited = [[0] * N for _ in range(N)]
  answer = 0
  for j in range(N):
    for k in range(N):
      if flooding_board[i][j][k] > i and visited[j][k] == 0:
        queue.append((j, k))
        visited[j][k] = 1
        bfs(i)
        answer += 1
  result.append(answer)

print(max(result))
