# 그리디 - 잃어버린 괄호

# equation = input().split('-')

# answer = 0
# for i in range(len(equation)):
#   equation[i] = equation[i].split('+')
#   for j in range(len(equation[i])):
#     if len(equation[i][j]) != 1:
#       equation[i][j] = int(equation[i][j].lstrip('0'))
#     else:
#       equation[i][j] = int(equation[i][j])
#   equation[i] = sum(equation[i])

# for i in range(len(equation)):
#   if i == 0:
#     answer += equation[i]
#   else:
#     answer += -equation[i]

# print(answer)

import sys
import re

eq = sys.stdin.readline()[:-1]

eq = re.sub('(0+)?([0-9]+)', '\\2', eq)
eq = re.sub('-([0-9]+(\+[0-9]+)+)', '-(\\1)', eq)
print(eval(eq))