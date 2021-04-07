# 그리디 - 주유소

N = int(input())
distances = list(map(int, input().split(' ')))
prices = list(map(int, input().split(' ')))

count = 0
current= 0
result = distances[0] * prices[0]
while count != len(distances)-1:
  if prices[current] <= prices[count+1]:
    result += distances[count+1] * prices[current]
  elif prices[current] > prices[count+1]:
    result += distances[count+1] * prices[count+1]
    current = count+1
  count += 1
print(result)