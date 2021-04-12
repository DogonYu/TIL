import sys
from collections import deque

N, K = map(int, sys.stdin.readline().split(' '))
queue = deque([(N, 0)])
visited = [0 for _ in range(100001)]
answer = 0

while queue:
  v, sec = queue.popleft()
  if v == K:
    answer = sec
    break
  if visited[v] == 0:
    if v+1 <= 100000:
      queue.append((v+1, sec+1))
    if 0 <= v-1 <= 100000:
      queue.append((v-1, sec+1))
    if v*2 <= 100000:
      queue.append((v*2, sec+1))
    visited[v] += 1

print(answer)
