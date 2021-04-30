# 기초 - 괄호

N = int(input())
ps = [input() for i in range(N)]

for i in range(len(ps)):
  stack = []
  iss = False
  for vps in ps[i]:
    if vps == '(':
      stack.append(vps)
    elif vps == ')':
      if stack:
        stack.pop()
      else:
        iss = True
        break
  if stack or iss:
    print('NO')
  else:
    print('YES')
