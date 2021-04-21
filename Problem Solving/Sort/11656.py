# 정렬 - 접미사 배열

import sys

txt = []
S = sys.stdin.readline().strip()

for i in range(len(S)):
  txt.append(S[i:])

print('\n'.join(map(str, sorted(txt))))