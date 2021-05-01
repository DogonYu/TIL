# 기초 - 요세푸스 문제 0

import sys
from collections import deque

N, K = map(int, sys.stdin.readline().strip().split(' '))
queue = deque([i for i in range(1, N+1)])
answer = []

while len(answer) != N:
  queue.rotate(-(K-1))
  answer.append(queue.popleft())

answer = ', '.join(map(str, answer))
print(f'<{answer}>')
