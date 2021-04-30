# 동적 프로그래밍 - 피보나치 수

import sys

sys.setrecursionlimit(10001)

def fibo(n):
  if n == 0:
    return 0
  if n <= 2:
    return 1
  if dp[n] == 0:
    dp[n] = fibo(n-1) + fibo(n-2)
    return dp[n]
  return dp[n]

N = int(sys.stdin.readline())
dp = [0] * 46

print(fibo(N))