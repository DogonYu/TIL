# 그리디 - 뒤집기

import sys

S = list(sys.stdin.readline().strip())

for i in range(len(S)-1):
  if S[i] == S[i+1]:
    S[i] = ''

print(min([S.count('0'), S.count('1')]))