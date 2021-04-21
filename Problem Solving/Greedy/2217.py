# 그리디 - 로프
'''
거꾸로 정렬해서 검사하는 이유

2개이상 고를 시 2번째로 큰 로프 중량의 최대값만 들 수 있기 때문임
'''
N = int(input())

lope_list = [int(input())for i in range(N)]

lope_list.sort(reverse=True)
answer = 0

for i in range(N):
  if lope_list[i] * (i+1) > answer:
    answer = lope_list[i] * (i+1)

print(answer)