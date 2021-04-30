# 기초 - 스택

import sys
N = int(sys.stdin.readline())

stack = []
for i in range(N):
  command = sys.stdin.readline()[:-1]
  if ' ' in command:
    command, num = command.split(' ')
  if 'push' in command:
    stack.append(num)
  elif 'pop' in command:
    if stack:
      print(stack.pop())
    else:
      print(-1)
  elif 'size' in command:
    print(len(stack))
  elif 'empty' in command:
    if stack:
      print(0)
    else:
      print(1)
  elif 'top' in command:
    if stack:
      print(stack[-1])
    else:
      print(-1)