# 정렬 - 30

import sys

N = sorted(sys.stdin.readline().strip(), reverse=True)
answer = 0

sum = sum(list(map(int, N)))
if sum % 3 == 0 and '0' in N:
  answer = int(''.join(N))
else:
  answer = -1

print(answer)