# 구현 - 문서 검색

import sys
import re

s = sys.stdin.readline().strip()
keyword = sys.stdin.readline().strip()
result = re.split(f'({keyword})', s)
answer = 0

for x in result:
  if x == keyword:
    answer += 1

print(answer)