# 중복되지 않는 순열
def permutation(arr, size, used):
    if len(used) == size:
        result.append(used[:])
        return
    
    for i in range(len(arr)):
        used.append(arr[i])
        temp = arr[:]
        temp.remove(arr[i])
        permutation(temp, size, used)
        used.pop()


result = []
permutation([1, 2, 3, 4, 5], 3, [])
print(len(result))