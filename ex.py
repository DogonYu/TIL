N = int(input())
cases = [input() for _ in range(N)]

score = []
answer = 0
temp = 0
for case in cases:
  for c in case:
    if c == 'O':
      temp += 1
    else:
      answer += temp
      temp = 0
  score.append(answer)
  answer = 0

print(score)