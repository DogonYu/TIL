# 동적 프로그래밍 - 1, 2, 3 더하기 3

import sys

T = int(sys.stdin.readline())
dp = [0] * 1000001
dp[1], dp[2], dp[3] = 1, 2, 4
for i in range(4, 1000001):
  dp[i] = (dp[i-3] + dp[i-2] + dp[i-1]) % 1000000009

for _ in range(T):
  N = int(sys.stdin.readline())
  print(dp[N])