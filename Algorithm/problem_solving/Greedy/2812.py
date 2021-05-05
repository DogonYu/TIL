# 그리디 - 크게 만들기

import sys

N, K = map(int, sys.stdin.readline().strip().split(' '))
num = sys.stdin.readline().strip()
stack = [num[0]]
cnt = K
for i in range(1, len(num)):
  while stack and K != 0 and stack[-1] < num[i]:
    stack.pop()
    K -= 1
  stack.append(num[i])

print(''.join(map(str, stack[:N-cnt])))