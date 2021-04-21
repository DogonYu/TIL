# 동적 프로그래밍 - 1로 만들기

import sys

dp = [0] * 1000002
N = int(sys.stdin.readline())

for i in range(2, N+1):
  dp[i] = dp[i-1] + 1
  if i % 2 == 0:
    dp[i] = min(dp[i], dp[i//2] + 1)
  if i % 3 == 0:
    dp[i] = min(dp[i], dp[i//3] + 1)

print(dp[N])