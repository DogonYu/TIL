# 구현 - 역원소 정렬

import sys

N = list(map(str, sys.stdin.readline().strip().split(' ')))
nums = [int(x[::-1]) for x in N[1:]]
N = int(N[0])

while len(nums) != N:
  x = list(map(str, sys.stdin.readline().strip().split(' ')))
  x = ' '.join(x).split()
  for i in x:
    nums.append(int(i[::-1]))

print('\n'.join(map(str, sorted(nums))))