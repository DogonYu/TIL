# 큐 - 카드2

import sys
from collections import deque

queue = deque([i for i in range(1, int(sys.stdin.readline())+1)])

while len(queue) != 1:
  queue.popleft()
  queue.rotate(-1)

print(*queue)