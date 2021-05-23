# 정렬 - Yangjojang of The Year

import sys

T = int(sys.stdin.readline())

for _ in range(T):
  N = int(sys.stdin.readline())
  schools = sorted([list(map(str, sys.stdin.readline().strip().split(' '))) for _ in range(N)], key=lambda x: -int(x[1]))

  print(schools[0][0])