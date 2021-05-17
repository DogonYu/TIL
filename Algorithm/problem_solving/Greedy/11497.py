# 구현 - 색종이

import sys

T = int(sys.stdin.readline())

for _ in range(T):
  N = int(sys.stdin.readline())
  logs = sorted(list(map(int, sys.stdin.readline().strip().split(' '))))

  mx = 0
  for i in range(2, N):
    mx = max(mx, abs(logs[i] - logs[i - 2]))
  print(mx)

'''
ex)
logs = [2, 4, 5, 7, 9] 비정렬
logs = [2, 5, 9, 7, 4] 정렬
x와 x-2가 통나무 높이 최대 차이
'''