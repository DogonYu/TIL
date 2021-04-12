import sys
from collections import deque

def bfs(y, x):
  queue = deque([(y, x)])
  visited.append((y,x ))
  cnt = 1
  while queue:
    vy, vx = queue.popleft()
    for dx, dy in (0,1),(0,-1),(1,0),(-1,0):
      ny, nx = vy+dy, vx+dx
      if 0 <= ny < N and 0 <= nx < N:
        if (ny, nx) not in visited and board[ny][nx] == 1:
          queue.append([ny, nx])
          visited.append((ny, nx))
          cnt += 1
  return cnt

N = int(sys.stdin.readline())
board = [list(map(int, sys.stdin.readline()[:-1])) for _ in range(N)]
visited = []
answer = []

for i in range(N):
  for j in range(N):
    if board[i][j] == 1 and (i,j) not in visited:
      answer.append(bfs(i,j))

print(len(answer))
print('\n'.join(map(str, sorted(answer))))