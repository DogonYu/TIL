# 중복되지 않는 순열
def permutation(arr, size, ele):
    
    if len(ele) == size:
        result.append(ele[:])
        return
    
    for i in range(len(arr)):
        ele.append(arr[i])
        temp = arr[:]
        temp.remove(arr[i])
        permutation(temp, size, ele)
        ele.pop()


result = []
permutation([1, 2, 3, 4, 5], 3, [])
print(len(result))