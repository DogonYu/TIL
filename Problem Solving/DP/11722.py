# 동적 프로그래밍 - 가장 긴 감소하는 부분 수열

import sys

N = int(sys.stdin.readline())
A = list(map(int, sys.stdin.readline().strip().split(' ')))
dp = [0] * 1001

