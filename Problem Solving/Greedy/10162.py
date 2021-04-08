# 그리디 - 전자레인지

time_list = [300, 60, 10]
count = [0, 0, 0]
T = int(input())

for i in range(len(time_list)):
  if T // time_list[i]:
    count[i] += T // time_list[i]
    T = T % time_list[i]

if T > 0:
  print(-1)
else:
  for c in count:
    print(c, end=' ')