# 정렬 - 수 정렬하기 3

import sys
N = int(sys.stdin.readline())
nums = [0 for _ in range(10001)]

for _ in range(N):
  num = int(sys.stdin.readline())
  nums[num] += 1

for i in range(len(nums)):
  if nums[i] > 0:
    for j in range(nums[i]):
      print(i)