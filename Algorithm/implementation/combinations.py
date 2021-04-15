# 조합
def combination(arr, size, used):
    if len(used) == size:
        result.append(used[:])
        return
    
    for i in range(len(arr)):
        used.append(arr[i])
        combination(arr[i+1:], size, used)
        used.pop()

result = []
combination([1, 2, 3, 4, 5], 3, [])
print(result)