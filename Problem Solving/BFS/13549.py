'''
다익스트라 알고리즘
0-1 BFS: 가중치가 0인 간선에 연결된 정점은 큐의 맨 뒤가 아닌 맨 앞에 넣는 방법
* 2를 별도의 간선으로 생각하지 않고, +1이나 -1에 의한 좌표를 큐에 넣을 때 그 좌표의 2의 거듭제곱 배인 좌표들을 전부 큐에 넣는 방법
'''

# BFS - 숨바꼭질 3

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
    if v*2 <= 100000:
      if sec == 0:
        queue.appendleft((v*2, sec))
      else:
        queue.append((v*2, sec))
    if 0 <= v-1 <= 100000:
      queue.append((v-1, sec+1))
    if v+1 <= 100000:
      queue.append((v+1, sec+1))
    visited[v] += 1

print(answer)