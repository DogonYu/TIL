# 정렬 - 베스트셀러

import sys

N = int(sys.stdin.readline())
books_list = [sys.stdin.readline().strip() for _ in range(N)]
books = {book:0 for book in books_list}

for book in books_list:
  books[book] += 1

print(sorted(books.items(), key=lambda x: (-x[1], x[0]))[0][0])