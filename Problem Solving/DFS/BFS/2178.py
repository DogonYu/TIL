import sys
from collections import deque

def bfs(x, y, visited):
  queue = deque([[x, y]])
<<<<<<< HEAD
  visited[x][y] = 1
  while queue:
    v = queue.popleft()
    for dx, dy in (1, 0), (-1, 0), (0, 1), (0, -1):
      nx, ny = v[0]+dx, v[1]+dy
      if 0 <= nx < N and 0 <= ny < M:
        if maze[nx][ny] == '1' and visited[nx][ny] == 0:
          visited[nx][ny] = visited[v[0]][v[1]] + 1
          queue.append([nx, ny])
  return visited[-1][-1]

maze = []
count = 0
N, M = map(int, sys.stdin.readline().split(' '))
visited = [[0 for _ in range(M)] for _ in range(N)]
for _ in range(N):
  maze.append(sys.stdin.readline()[:M])

print(bfs(0, 0, visited))
=======
  while queue:
    v = queue.popleft()
    for dx, dy in (1, 0), (0, 1), (0, -1), (-1, 0):
      nx, ny = v[0]+dx, v[1]+dy
      if nx < 0 or ny < 0 or nx >= N or ny >= M:
        continue
      if maze[nx][ny] == '1':
        if [nx, ny] not in visited:
          visited.append([nx, ny])
          queue.append([nx, ny])

visited = [[0, 0]]
maze = []
count = 0
N, M = map(int, sys.stdin.readline().split(' '))
for _ in range(N):
  maze.append(sys.stdin.readline()[:M])

bfs(0, 0, visited)
print(visited)
for v in visited:
  count += 1
  if [N-1, M-1] == v:
    break
print(count)
>>>>>>> e7c163906e4291095af45c6ea81ee27182dbf472
