# 스타트와 링크

import sys
from itertools import combinations

N = int(sys.stdin.readline())
board = [list(map(int, sys.stdin.readline().strip().split(' '))) for _ in range(N)]
comb = list(combinations([i for i in range(N)], N//2))
comb = [[comb[i], comb[-1-i]] for i in range(len(comb))]
answer = []
for x in comb:
  temp1 = 0
  temp2 = 0
  team1 = list(combinations(list([i for i in x[0]]), 2))
  team2 = list(combinations(list([i for i in x[1]]), 2))
  for i in team1:
    temp1 += board[i[0]][i[1]] + board[i[1]][i[0]]
  for i in team2:
    temp2 += board[i[0]][i[1]] + board[i[1]][i[0]]
  answer.append((temp1, temp2))
answer = sorted(answer, key=lambda x: abs(x[0]-x[1]))
print(abs(answer[0][0] - answer[0][1]))