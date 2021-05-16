# 정렬 - 점수 계산

import sys

nums = [int(sys.stdin.readline()) for _ in range(8)]
sorted_nums = sorted(nums)
answer = []

print(sum(sorted_nums[-5:]))
for x in sorted_nums[-5:]:
  answer.append(nums.index(x) + 1)

print(' '.join(map(str, sorted(answer))))
