# 정렬 - 듣보잡

import sys

N, M = map(int, sys.stdin.readline().strip().split(' '))
_list = [sys.stdin.readline().strip() for _ in range(N+M)]
dict = {x:0 for x in _list}
answer = []

for x in _list:
  dict[x] += 1

for x, y in dict.items():
  if y > 1:
    answer.append(x)

answer.sort()
print(len(answer))
print('\n'.join(map(str, answer)))