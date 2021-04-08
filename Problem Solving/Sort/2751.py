# 정렬 - 수 정렬하기2

import sys
N = int(sys.stdin.readline())
nums = [int(sys.stdin.readline()) for _ in range(N)]

for num in sorted(nums):
  print(num)