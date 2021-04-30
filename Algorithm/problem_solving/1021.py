# 덱 - 회전하는 큐

import sys
from collections import deque

N, M = map(int, sys.stdin.readline().split(' '))
target = list(map(int, sys.stdin.readline().split(' ')))
d = deque([i for i in range(1, N+1)])
answer = 0
i = 0

while len(d) != N - len(target):
  left, right = 0, 0
  if target[i] == d[0]:
    d.popleft()
    i += 1
  else:
    for j in range(len(d)):
      if target[i] == d[j]:
        left, right = j, len(d)-j
        break
    if left < right:
      d.rotate(-left)
      answer += left
    else:
      d.rotate(right)
      answer += right
print(answer)