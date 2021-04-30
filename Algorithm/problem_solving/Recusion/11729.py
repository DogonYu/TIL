# 재귀 - 하노이 탑

import sys

def hanoi(start, end, n):
  if n == 0:
    return
  hanoi(start, 6-start-end, n-1)
  print(start, end)
  hanoi(6-start-end, end, n-1)

n = int(sys.stdin.readline())

print(2 ** n - 1)
hanoi(1, 3, n)