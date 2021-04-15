# 조합
def combination(arr, size, ele):
    if len(ele) == size:
        result.append(ele[:])
        return
    
    for i in range(len(arr)):
        ele.append(arr[i])
        combination(arr[i+1:], size, ele)
        ele.pop()

result = []
combination([1, 2, 3, 4, 5], 3, [])
print(result)