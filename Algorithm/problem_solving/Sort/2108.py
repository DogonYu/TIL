# 정렬 - 통계학

import sys
from collections import Counter

N = int(sys.stdin.readline())
nums = sorted([int(sys.stdin.readline()) for _ in range(N)])
counter = Counter(nums)

print(round(sum(nums)/N))
print(nums[len(nums)//2])

current = list(sorted(counter, key=lambda x: -counter[x]))[0]
result = []
for key in counter.keys():
  if counter[current] == counter[key]:
    result.append(counter[key])
  elif counter[current] < counter[key]:
    result = []
    current = counter[key]
    result.append(counter[key])
if len(counter) == len(result):
  if len(result) > 1:
    print(list(sorted(counter, key=lambda x: -counter[x]))[1])
  else:
    print(list(sorted(counter, key=lambda x: -counter[x]))[0])
else:
  if len(result) > 1:
    print(list(sorted(counter, key=lambda x: -counter[x]))[1])
  else:
    print(list(sorted(counter, key=lambda x: -counter[x]))[0])

print(max(nums) - min(nums))