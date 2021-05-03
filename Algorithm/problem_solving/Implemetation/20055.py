# 구현 - 결혼식

import sys
from collections import deque

def bfs(x):
  visited = [0] * (n+1)
  visited[x] = 1
  queue.append(x)
  while queue:
    v = queue.popleft()
    for i in friend[v]:
      if not visited[i]:
        visited[i] = visited[v] + 1
        queue.append(i)
  return visited

n = int(sys.stdin.readline())
m = int(sys.stdin.readline())
friend = [[] for _ in range(n+1)]
queue = deque()
for _ in range(m):
  a, b = map(int, sys.stdin.readline().strip().split(' '))
  friend[a].append(b)
  friend[b].append(a)

answer = bfs(1)
cnt = 0
for x in answer:
  if 1 < x <= 3:
    cnt += 1
print(cnt)