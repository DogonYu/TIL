import sys

def check(x, y):
  temp = []
  cnt = 1
  current = 0
  j = current + 1
  for _ in range(N):
    if current < j < N:
      if board[y][current] == board[y][j]:
        cnt += 1
        j += 1
      else:
        current += 1
        j = current + 1
        cnt = 1
    temp.append(cnt)

  cnt = 1
  current = 0
  j = current + 1
  for _ in range(N):
    if current < j < N:
      if board[current][x] == board[j][x]:
        cnt += 1
        j += 1
      else:
        current += 1
        j = current + 1
        cnt = 1
    temp.append(cnt)
  return max(temp)


def change_candy(x, y):
  result = 0
  for dx, dy in (0, 1), (0, -1), (1, 0), (-1, 0):
    nx, ny = x+dx, y+dy
    if 0 <= nx < N and 0 <= ny < N:
      board[y][x], board[ny][nx] = board[ny][nx], board[y][x]
      if result < check(nx, ny):
        result = check(nx, ny)
      board[y][x], board[ny][nx] = board[ny][nx], board[y][x]
  return result


N = int(sys.stdin.readline())
board = [list(sys.stdin.readline()[:-1]) for _ in range(N)]
answer = []

for i in range(len(board)):
  for j in range(len(board[i])):
    answer.append(change_candy(i, j))

print(max(answer))