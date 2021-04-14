import sys

def solution(phone_book):
  phone_book.sort()
  for i in range(len(phone_book)-1):
    if phone_book[i+1].startswith(phone_book[i]):
      return 'NO'
  return 'YES'

T = int(sys.stdin.readline())
for _ in range(T):
  N = int(sys.stdin.readline())
  phone_book = [sys.stdin.readline()[:-1] for _ in range(N)]
  print(solution(phone_book))