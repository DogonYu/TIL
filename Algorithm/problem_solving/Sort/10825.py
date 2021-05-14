# 정렬 - 국영수

import sys

N = int(sys.stdin.readline())
grades = sorted([sys.stdin.readline().strip().split(' ') for _ in range(N)], key=lambda x: (-int(x[1]), int(x[2]), -int(x[3]), str(x[0])))

for x in grades:
  print(x[0])