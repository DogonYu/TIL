# 정렬 - 중복 뱨고 정렬하기

import sys

N = int(sys.stdin.readline())
nums = sorted(list(set(map(int, sys.stdin.readline().strip().split(' ')))))

print(' '.join(map(str, nums)))