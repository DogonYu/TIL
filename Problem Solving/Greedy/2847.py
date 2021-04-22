# 그리디 - 게임을 만든 동준이

import sys

N = int(sys.stdin.readline())
score = [int(sys.stdin.readline().strip()) for _ in range(N)][::-1]
answer = 0

for i in range(len(score)-1):
  if score[i] <= score[i+1]:
    answer += score[i+1] - score[i] + 1
    score[i+1] -= score[i+1] - score[i] + 1

print(answer)