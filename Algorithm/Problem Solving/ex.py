import sys
import math

def is_prime_number(st, n):
  array = [True for i in range(n+1)]
  array[1] = False
  for i in range(2, int(math.sqrt(n)) + 1):
    if array[i] == True:
      j = 2
      while i * j <= n:
        array[i * j] = False
        j += 1

  return [i for i in range(st, n+1) if array[i]]

N, M = map(int, sys.stdin.readline().strip().split(' '))

print('\n'.join(map(str, is_prime_number(N, M))))