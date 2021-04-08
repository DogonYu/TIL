# 정렬 - 좌표 압축

import sys
N = int(sys.stdin.readline())

X = list(map(int, sys.stdin.readline().split(' ')))
Xi = list(sorted(set(X)))
Xi = {Xi[i]:i for i in range(len(Xi))}

for i in X:
  print(Xi[i], end=' ')