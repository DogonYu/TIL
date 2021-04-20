'''
기수 정렬
1의 자리 -> 10의자리 -> ... 순으로 정렬
D는 자릿수의 최대 개수 일때, O(DN)
공간의 낭비가 심해서 보통 vector나 연결 리스트로 구현함
구현할 일 별로 없어서 이론만..
'''
def digit_num(x, a):
  return int((x / p10[a]) % 10)

def radix_sort(d):
  temp = [0] * len(list)
  p10[0] = 1
  for i in range(1, d):
    p10[i] = p10[i-1] * 10
  for i in range(d):
    for j in range(10):
      digit[j] = []
    for j in range(len(list)):
      digit[digit_num(list[j], i)].append(list[j])
    idx = 0
    for j in range(10):
      for x in digit[j]:
        temp[idx] = x
        idx += 1
  return temp

list = [312, 234, 512, 100, 999]
digit = [[] for _ in range(10)]
p10 = [0] * 3

print(radix_sort(3))