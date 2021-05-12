# 그리디 - 폴리오미노

import sys
import re

board = sys.stdin.readline().strip()
board_length = len(board)
board = re.split('([.]+)', board)
answer = ''
for x in board:
  temp = len(x)
  if 'X' in x:
    if temp // 4 > 0:
      answer += ('A' * 4) * (temp // 4)
      temp -= 4 * (temp // 4)
    if temp != 0 and temp // 2 > 0:
      answer += ('B' * 2) * (temp // 2)
      temp -= 2 * (temp // 2)
  else:
    answer += x

if board_length == len(answer):
  print(answer)
else:
  print(-1)