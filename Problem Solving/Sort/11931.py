# 정렬 - 수 정렬하기 4

import sys

N = int(sys.stdin.readline())
nums = [int(sys.stdin.readline()) for _ in range(N)]

print('\n'.join(map(str, sorted(nums, reverse=True))))