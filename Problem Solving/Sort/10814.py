# 정렬 - 나이순 정렬

import sys

N = int(sys.stdin.readline())
xy = [tuple(sys.stdin.readline()[:-1].split(' ')) for _ in range(N)]

for x, y in sorted(xy, key=lambda x: (int(x[0]))):
  print(x, y)