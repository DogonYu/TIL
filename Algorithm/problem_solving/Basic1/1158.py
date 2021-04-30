# 기초 - 요세푸스 문제

import sys
from collections import deque

N, M = map(int, sys.stdin.readline().split(' '))
queue = deque([i for i in range(1, N+1)])
i = 0
answer = []
while queue:
  q = queue.popleft()
  i += 1
  if i == M:
    answer.append(q)
    i = 0
  else:
    queue.append(q)

print('<', end='')
for i in range(len(answer)):
  if i != len(answer)-1:
    print(answer[i], end=', ')
  else:
    print(answer[i], end='')
print('>')