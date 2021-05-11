import sys

N, M = map(int, sys.stdin.readline().strip().split(' '))
poketmon_list = [sys.stdin.readline().strip() for i in range(N)]
poketmon_hash = {poketmon_list[i]:i+1 for i in range(len(poketmon_list))}
problem = [sys.stdin.readline().strip() for _ in range(M)]
print(poketmon_list)
for x in problem:
  if x.isdigit():
    print(poketmon_list[int(x)-1])
  else:
    print(poketmon_hash[x])