def quick_sort(st, en):
  if en <= st+1:
    return
  pivot = list[st]
  l, r = st + 1, en-1
  while True:
    while list[l] <= pivot and l <= r:
      l += 1
    while list[r] >= pivot and l <= r:
      r -= 1
    if l > r:
      break
    list[l], list[r] = list[r], list[l]
  list[st], list[r] = list[r], list[st]
  quick_sort(st, r)
  quick_sort(r+1, en)

list = [6, -8, 1, 12, 8, 3, 7, -7]

quick_sort(0, len(list))
print(list)