# 그리디 - 회의실 배정

N = int(input())

meet_list = []
for _ in range(N):
  meet_list.append(list(map(int, input().split(' '))))

count = 0
end_meet = meet_list[count][1]
start_meet = meet_list[count+1][0]
answer = 1
while count != len(meet_list):
  # print(end_meet, start_meet)
  if end_meet <= start_meet:
    end_meet = meet_list[count+1][1]
    answer += 1
  count += 1
  if count+1 < len(meet_list):
    start_meet = meet_list[count+1][0]    

print(answer)