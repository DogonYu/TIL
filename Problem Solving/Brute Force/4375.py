# 완전탐색 - 1

while True:
  try:
    N = int(input())
  except EOFError:
    break
  if N == 1:
    print(1)
    continue
  num = 1
  while True:
    num = num * 10 + 1
    if num % N == 0:
      print(len(str(num)))
      break
