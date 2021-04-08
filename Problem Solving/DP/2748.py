# DP - 피보나치 수 2

fi = [0 for _ in range(91)]

def fibo(num):
  if num <= 1:
    fi[num] = num

  elif fi[num] == 0:
    fi[num] = fibo(num-1) + fibo(num-2)
    
  return fi[num]

num = int(input())

print(fibo(num))