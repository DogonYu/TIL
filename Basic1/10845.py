import sys
N = int(sys.stdin.readline())

queue = []
for i in range(N):
  command = sys.stdin.readline()[:-1]
  if ' ' in command:
    command, num = command.split(' ')
  if 'push' in command:
    queue.append(num)
  elif 'pop' in command:
    if queue:
      print(queue.pop(0))
    else:
      print(-1)
  elif 'size' in command:
    print(len(queue))
  elif 'empty' in command:
    if queue:
      print(0)
    else:
      print(1)
  elif 'front' in command:
    if queue:
      print(queue[0])
    else:
      print(-1)
  elif 'back' in command:
    if queue:
      print(queue[-1])
    else:
      print(-1)