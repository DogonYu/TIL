# 그리디 - 1946

import sys

T = int(sys.stdin.readline())

for _ in range(T):
  N = int(sys.stdin.readline())
  nums = sorted([list(map(int, sys.stdin.readline().strip().split(' '))) for _ in range(N)], key=lambda x: x[0])
  min = nums[0][1]
  answer = 1
  
  for i in range(1, len(nums)):
    if nums[i][1] < min:
      min = nums[i][1]
      answer += 1

  print(answer)