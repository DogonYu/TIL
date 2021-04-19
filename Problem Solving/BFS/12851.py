# BFS - 숨바꼭질 2

import sys
from collections import deque

N, K = map(int, sys.stdin.readline().split(' '))
answer = 0
cnt = 0
queue = deque([(N, 0)])
visited = []

while queue:
  v, sec = queue.popleft()
  if v == K:
    answer = sec
    break
  if (v, sec) not in visited:
    if v*2 <= 100000:
      queue.append((v*2, sec+1))
    if 0 <= v-1 <= 100000:
      queue.append((v-1, sec+1))
    if v+1 <= 100000:
      queue.append((v+1, sec+1))
    visited.append((v, sec, 1))
  elif (v, sec) in visited:
    visited[visited.index((v, sec))][2] += 1


print(visited)
while visited:
  v, sec, a = visited.pop(0)
  if v*2 == K and answer-1 == sec:
    cnt += 1
  if v+1 == K and answer-1 == sec:    
    cnt += 1
  if v-1 == K and answer-1 == sec:
    cnt += 1

print(answer)
print(cnt)