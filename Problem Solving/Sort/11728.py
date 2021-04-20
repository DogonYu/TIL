# 정렬 - 배열 합치기

import sys

N, M = map(int, sys.stdin.readline().strip().split(' '))

A = list(map(int, sys.stdin.readline().strip().split(' ')))
B = list(map(int, sys.stdin.readline().strip().split(' ')))
answer = []
cursor1, cursor2 = 0, 0
for _ in range(len(A)+len(B)):
  if cursor1 == len(A):
    answer.append(B[cursor2])
    cursor2 += 1
  elif cursor2 == len(B):
    answer.append(A[cursor1])
    cursor1 += 1
  elif A[cursor1] < B[cursor2]:
    answer.append(A[cursor1])
    cursor1 += 1
  else:
    answer.append(B[cursor2])
    cursor2 += 1
print(' '.join(map(str, answer)))