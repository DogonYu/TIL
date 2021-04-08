N, M, K = map(int, input().split(' '))

while K != 0:
  if N > M:
    N -= K
    K -= K
    if N < 3:
      N += 2
      K += 2
  else:
    M -= K
    K -= K
    if M == 0:
      M += 1
      K += 1

if N // 2 <= M:
  print(N//2)
elif M == 1 and N // 2 > 0:
  print(1)