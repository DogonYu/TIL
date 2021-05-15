# 아분탐색 - 예산

import sys

N = int(sys.stdin.readline())
budget = sorted(list(map(int, sys.stdin.readline().strip().split(' '))))
M = int(sys.stdin.readline())
st, en = 1, budget[-1]

while st <= en:
  mid = (st + en) // 2
  mx_budget = 0

  for x in budget:
    if x > mid:
      mx_budget += mid
    else:
      mx_budget += x

  if mx_budget <= M:
    st = mid + 1
  else:
    en = mid - 1

print(en)