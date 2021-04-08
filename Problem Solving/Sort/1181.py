# 정렬 - 단어 정렬

count = int(input())
arr = []

for i in range(count):
    str = input()
    arr.append((len(str), str))

arr = set(arr)
arr = sorted(arr)

for i, j in arr:
    print(j)