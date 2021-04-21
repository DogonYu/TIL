# 그리디 - 보물

N = int(input())

A = sorted(list(map(int, input().split(' '))))
B = list(reversed(sorted(list(map(int, input().split(' '))))))
answer = 0
for a, b in zip(A, B):
  answer += a * b
print(answer)