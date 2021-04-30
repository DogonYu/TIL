# 그리디 - 거스름돈

money = 1000 - int(input())
answer = 0
coin_list = [500, 100, 50, 10, 5, 1]

for coin in coin_list:
  if money // coin:
    answer += money // coin
    money = money % coin

print(answer)
