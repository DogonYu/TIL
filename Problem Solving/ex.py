import sys

# N = int(sys.stdin.readline())
# informations = [list(map(int, sys.stdin.readline()[:-1].split(' '))) for _ in range(N)]

# print(informations)

# N = int(sys.stdin.readline())
# divisors = [i for i in range(1, N+1)]
# answer = 0

# for i in divisors:
#   answer += (N // i) * i
# print(answer)

T = int(sys.stdin.readline())
dp = [0] * 1000000
for i in range(1, N+1):
  answer += (N // i) * i

for _ in range(T):
  answer = 0
  N = int(sys.stdin.readline())
  print(dp[N])
