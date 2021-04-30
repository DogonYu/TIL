# 동적 프로그래밍 - RGB거리

import sys

N = int(sys.stdin.readline())
R, G, B = [], [], []
for _ in range(N):
  red, green, blue = map(int, sys.stdin.readline().strip().split(' '))
  R.append(red)
  G.append(green)
  B.append(blue)
dp = [[0] * N for _ in range(N)]
dp[0][0] = R[0]
dp[0][1] = G[0]
dp[0][2] = B[0]

for i in range(1, N):
  dp[i][0] = min(dp[i-1][1], dp[i-1][2]) + R[i]
  dp[i][1] = min(dp[i-1][0], dp[i-1][2]) + G[i]
  dp[i][2] = min(dp[i-1][0], dp[i-1][1]) + B[i]

print(min(dp[N-1][0], dp[N-1][1], dp[N-1][2]))