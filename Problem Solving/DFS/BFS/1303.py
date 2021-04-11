import sys
from collections import deque

def bfs(x, y, color, visited):
  count = 1
  queue = deque()
  queue.append([x,y])
  while queue:
    v = queue.popleft()
    for dx, dy in (1, 0), (-1, 0), (0, -1), (0, 1):
      nx, ny = v[0]+dx, v[1]+dy
      if nx < 0 or ny < 0 or nx >= M or ny >= N:
        continue
      if color == soldiers[nx][ny]:
        if [nx, ny] not in visited:
          visited.append([nx, ny])
          queue.append([nx, ny])
          count += 1
  return [sorted(visited, key=lambda x: (x[0], x[1])), count]

N, M = map(int, sys.stdin.readline().split(' '))

soldiers = []
visited = []
mine = 0
your = 0
for _ in range(M):
  soldiers.append(sys.stdin.readline()[:N])

for i in range(len(soldiers)):
  for j in range(len(soldiers[i])):
    if [i, j] not in visited and soldiers[i][j] == 'W':
      visited.append([i,j])
      visited, count = bfs(i, j, soldiers[i][j], visited)
      mine += count ** 2

visited = []
for i in range(len(soldiers)):
  for j in range(len(soldiers[i])):
    if [i, j] not in visited and soldiers[i][j] == 'B':
      visited.append([i,j])
      visited, count = bfs(i, j, soldiers[i][j], visited)
      your += count ** 2

print(mine)
print(your)