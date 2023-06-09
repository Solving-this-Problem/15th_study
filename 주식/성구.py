# 11501 주식 - Greedy
import sys
input = sys.stdin.readline
# 테스트 케이스 돌리기
for _ in range(int(input())):
    N = int(input())
    days = list(map(int, input().split()))
    max_price = days[-1]  # 초기 최댓값은 마지막 수
    benefit = 0 # 얻을 수 있는 이득
    for day in range(N-1, -1, -1):
        if max_price < days[day]:   # 만약 값이 최대보다 크면 최댓값 바꾸기(팔기 수행)
            max_price = days[day]
        else:
            benefit += max_price-days[day]  # 최대보다 작거나 같다면 이득에 최대와의 차이 추가하기(사기 수행)
    print(benefit)