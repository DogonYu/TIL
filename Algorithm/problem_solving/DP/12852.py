# 동적 프로그래밍 - 1로 만들기 2

import sys

N = int(sys.stdin.readline())
dp = [0] * 1000001
pre = [0] * 1000001
for i in range(2, N+1):
  dp[i] = dp[i-1] + 1
  pre[i] = i-1
  if i % 3 == 0 and dp[i] > dp[i//3] + 1:
    dp[i] = dp[i//3] + 1
    pre[i] = i//3
  if i % 2 == 0 and dp[i] > dp[i//2] + 1:
    dp[i] =dp[i//2] + 1
    pre[i] = i//2

print(dp[N])
cur = N
while cur != 0:
  print(cur, end=' ')
  cur = pre[cur]