# 스택 - 옥상 정원 꾸미기

import sys

N = int(sys.stdin.readline())
nums = [int(sys.stdin.readline()) for _ in range(N)]
answer = 0
stack = []

for i in range(N):
  while stack and stack[-1] <= nums[i]:
    stack.pop()
  stack.append(nums[i])
  answer += len(stack)-1

print(answer)