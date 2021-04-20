# 정렬 - 수 정렬하기 5

import sys

N = int(sys.stdin.readline())
nums = [int(sys.stdin.readline()) for _ in range(N)]
counting = [0] * 2000001

for x in nums:
  counting[x+1000000] += 1

for i in range(len(counting)):
  if counting[i] > 0:
    for _ in range(counting[i]):
        print(i - 1000000)