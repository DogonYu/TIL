'''
카운팅 정렬
크기가 대략 1000만 이하일 때 사용 가능한 정렬
메모리를 많이 사용하게 됨
K는 카운팅 된 수의 범위일 때, 시간 복잡도가 O(N+K)
'''
def counting_sort(list):
  counting = [0] * 2000001
  temp = []
  for x in list:
    counting[x+1000000] += 1

  for i in range(len(counting)):
    if counting[i] > 0:
      for _ in range(counting[i]):
          temp.append(i - 1000000)
  return temp

list = [-1, 9 ,3, 3, 1, -10]
print(counting_sort(list))