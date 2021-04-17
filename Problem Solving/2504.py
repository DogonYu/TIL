# 스택 - 괄호의 값

import sys

s = sys.stdin.readline().strip()
stack = []
result = []
answer = 0
depth = 1

for x in s:
  if not stack:
    if x == ')' or x == ']':
      answer = 0
      break
  if x == '(':
    stack.append(x)
    result.append([depth, 2])
    depth += 1
  elif x == '[':
    stack.append(x)
    result.append([depth, 3])
    depth += 1
  elif x == ')':
    if stack.pop() == '[':
      answer = 0
      break
    depth -= 1
  elif x == ']':
    if stack.pop() == '(':
      answer = 0
      break
    depth -= 1
  else:
    answer = 0
    break
  if not stack:
    temp = 0
    same = []
    while True:
      v = result.pop()
      if same and same[-1][0] == v[0]:
        idx, value = same.pop()
        result.append(v)
        result.append([idx, value])
        continue
      if not result:
        answer += v[-1]
        break
      if result[-1][0] < v[0]:
        temp = v[1] * result[-1][1]
        result.append([result.pop()[0], temp])
      elif result[-1][0] == v[0]:
        idx, value = result.pop()
        temp = value + v[1]
        result.append([idx, temp])
      else:
        same.append([v[0], v[1]])

if stack:
  answer = 0
print(answer)