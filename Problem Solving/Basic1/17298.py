import sys

N = int(sys.stdin.readline())
a = list(map(int, sys.stdin.readline().split(' ')))
stack = [0]
result = [-1 for _ in range(N)]
i = 1

while stack and i < N:
  while stack and a[stack[-1]] < a[i]:
    result[stack[-1]] = a[i]
    stack.pop()
  stack.append(i)
  i += 1

for n in result:
  print(n, end=' ')