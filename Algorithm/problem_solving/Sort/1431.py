# 정렬 - 시리얼 번호

import sys

N = int(sys.stdin.readline())
serials = [sys.stdin.readline().strip() for _ in range(N)]

print('\n'.join(sorted(serials, key=lambda s: (len(s), sum(int(x) for x in s if x.isdigit()), s))))