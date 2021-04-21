# 동적 프로그래밍 - 2xn 타일링

import sys

N = int(sys.stdin.readline())
dp = [0] * (N+1)
if N <= 2:
  print(N)
  exit()
dp[1] = 1
dp[2] = 2
for i in range(3, N+1):
  dp[i] = (dp[i-1] + dp[i-2]) % 10007

print(dp[N])