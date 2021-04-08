# 정렬 - 수 정렬하기

N = int(input())
nums = [int(input()) for _ in range(N)]

for num in sorted(nums):
  print(num)