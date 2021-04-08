N = int(input())
nums = sorted([int(input()) for _ in range(N)])
set_nums = list(set(nums))
min_list = []
max_num = 0

print(sum(nums)//N)
print(nums[len(nums)//2])
for num in set_nums:
  min_list.append(nums.count(num))
  if max_num < nums.count(num):
    max_num = nums.count(num)
if len(min_list) == 1:
  print(nums[0]) 
elif min_list.count(max_num) == len(min_list):
  print(nums[1])
else:
  answer = min_list.index(max(min_list)) + 1
  print(set_nums[answer])
print(max(nums)-min(nums))