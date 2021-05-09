# 정렬 - K번째 수

import sys

N, K = map(int, sys.stdin.readline().strip().split(' '))
A = sorted(list(map(int, sys.stdin.readline().strip().split(' '))))
print(A[K-1])