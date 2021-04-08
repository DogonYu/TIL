# 기초 - 프린터 큐

import sys
from collections import deque

input = sys.stdin.readline
N = int(input())

for _ in range(N):
  result = 1
  M, K = map(int, input().split(' '))
  I = list(map(int, input().split(' ')))
  index_queue = deque([i for i in range(len(I))])
  values_queue = deque([I[i] for i in range(len(I))])
  # print(index_queue, values_queue)
  while values_queue:
    if max(values_queue) > values_queue[0]:
      values_queue.append(values_queue.popleft())
      index_queue.append(index_queue.popleft())
    else:
      if index_queue[0] == K:
        print(result)
        break
      result += 1
      values_queue.popleft()
      index_queue.popleft()