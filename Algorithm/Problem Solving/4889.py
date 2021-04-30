# 스택 - 안정적인 문자열

import sys

count = 1
while True:
  answer = 0
  stack = []
  s = list(sys.stdin.readline()[:-1])
  if '-' in s:
    break
  for x in s:
    if not stack and x == '}':
      stack.append('{')
      answer += 1
    elif x == '{':
      stack.append('{')
    elif x == '}':
      stack.pop()
  
  while stack:
    if stack[-1] == '{':
      stack[-1] = '}'
      answer += 1
    elif stack[-2] == '{' and stack[-1] == '}':
      stack.pop()
      stack.pop()

  print(f'{count}. {answer}')
  count += 1
