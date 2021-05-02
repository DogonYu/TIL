# 구현 - 겉넓이 구하기

import sys

N, M = map(int, sys.stdin.readline().strip().split(' '))
board = [list(map(int, sys.stdin.readline().strip().split(' '))) for _ in range(N)]
up, left, front = N * M, 0, 0

for i in range(M):
  for j in range(N):
    if j == 0:
      front += board[j][i]
    else:
      if board[j-1][i] < board[j][i]:
        front += board[j][i] - board[j-1][i]

for i in range(N):
  for j in range(M):
    if j == 0:
      left += board[i][j]
    else:
      if board[i][j-1] < board[i][j]:
        left += board[i][j] - board[i][j-1]
  
answer = 2 * (up + left + front)
print(answer)