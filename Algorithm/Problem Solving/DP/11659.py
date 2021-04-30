# 동적 프로그래밍 - 구간 합 구하기 4

import sys

N, M = map(int, sys.stdin.readline().strip().split(' '))
nums = list(map(int, sys.stdin.readline().strip().split(' ')))
dp = [0] * (N+1)
dp[0] = 0
for i in range(1, N+1):
  dp[i] = dp[i-1] + nums[i-1]
print(dp)
for _ in range(M):
  i, j = map(int, sys.stdin.readline().strip().split(' '))
  print(dp[j] - dp[i-1])