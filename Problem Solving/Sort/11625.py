# 정렬 - 카드

import sys

N = int(sys.stdin.readline())
nums = sorted([int(sys.stdin.readline()) for _ in range(N)])
t = nums[0]
count = 1
answer = []

for i in range(1, len(nums)):
  if t < nums[i]:
    answer.append((t, count))
    t = nums[i]
    count = 1
  else:
    count += 1
answer.append((t, count))

print(sorted(answer, key=lambda x: -x[1])[0][0])
