# 정렬 - 좌표 정렬하기

import sys

N = int(sys.stdin.readline())
xy = [list(map(int, sys.stdin.readline()[:-1].split(' '))) for _ in range(N)]

for x, y in sorted(xy, key=lambda x: (x[0], x[1])):
  print(x, y)