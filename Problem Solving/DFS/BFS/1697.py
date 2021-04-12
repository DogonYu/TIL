import sys
from collections import deque

<<<<<<< HEAD
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
=======
def bfs(graph, start, visited):
  queue = deque([start])
  while queue:
    v = queue.popleft()
    for i in graph[v]:
      if i not in visited:
        queue.append(i)
        visited.append(i)

N, K = map(int, sys.stdin.readline().split(' '))

>>>>>>> e7c163906e4291095af45c6ea81ee27182dbf472
