# 스택 - 탑

import sys

N = int(sys.stdin.readline())
nums = list(map(int, sys.stdin.readline()[:-1].split(' ')))
stack = []
answer = []

for i in range(N):
    while stack:
        if stack[-1][1] > nums[i]:
            answer.append(stack[-1][0] + 1)
            break
        else:
            stack.pop()
    if not stack:
        answer.append(0)
    stack.append([i, nums[i]])

print(*answer)