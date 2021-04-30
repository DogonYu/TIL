# 동적 프로그래밍 - 계단 오르기

import sys

N = int(sys.stdin.readline())
score = [int(sys.stdin.readline()) for _ in range(N)]

# dp = [[0] * 2 for _ in range(N+1)]
# if N == 1:
#   print(score[0])
#   exit()
# dp[0][0] = score[0]
# dp[0][1] = 0
# dp[1][0] = score[1]
# dp[1][1] = score[0] + score[1]

# for i in range(2, N):
#   dp[i][0] = max(dp[i-2][0], dp[i-2][1]) + score[i]
#   dp[i][1] = dp[i-1][0] + score[i]

# print(max(dp[N-1][0], dp[N-1][1]))

dp = [0] * (N-1)
if N <= 2:
  print(sum(score))
  exit()
dp[0] = score[0]
dp[1] = score[1]
dp[2] = score[2]
for i in range(3, N-1):
  dp[i] = min(dp[i-2], dp[i-3]) + score[i]

print(sum(score) - min(dp[N-2], dp[N-3]))