# 그리디 - 설탕 배달

'''
5kg과 3kg 중 5kg이 더 크기 때문에 나눠지면 바로 answer로 출력

3kg부터 빼는 이유
작은 수부터 빼야 더 정밀하게 확인 가능
'''

N = int(input())

answer = 0
if N % 5 == 0:
  answer = N // 5
else:
  while True:
    N -= 3
    if N < 0:
      answer = -1
      break
    answer += 1
    if N % 5 == 0:
      answer += N // 5
      break

print(answer)