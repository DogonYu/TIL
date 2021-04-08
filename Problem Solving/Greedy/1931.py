# 그리디 - 회의실 배정
import sys
N = int(sys.stdin.readline())

meet_list = []
answer = 1
for _ in range(N):
  meet_list.append(list(map(int, sys.stdin.readline().split(' '))))

meet_list = sorted(meet_list, key=lambda x: (x[1], x[0]))
start, end = meet_list.pop(0)
for meet in meet_list:
  if end <= meet[0]:
    end = meet[1]
    answer += 1
  elif meet[1] <= start:
    start = meet[0]
    answer += 1

print(answer)