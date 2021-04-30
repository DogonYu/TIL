# 그리디 - 동전0
'''
소지한 돈을 내림차순 동전으로 나누는 이유

제일 큰 동전으로 거슬러 줘야하기 때문에 내림차순으로 정률 후 나눔
나누면 몫은 동전의 개수이기 때문임
'''

N, K = map(int, input().split())
answer = 0
coin_list = [int(input())for i in range(N)]

coin_list.sort(reverse=True)
for i in range(N):
    if K // coin_list[i] > 0:
        answer += K // coin_list[i]
        K -= coin_list[i] * (K // coin_list[i])

print(answer)
