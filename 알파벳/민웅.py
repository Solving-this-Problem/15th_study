#11501_주식_stock
import sys
input = sys.stdin.readline

T = int(input())

for tc in range(T):
    N = int(input())

    nli = list(map(int, reversed(input().split())))

    ans = 0
    max_num = 0
    for i in range(N):
        if nli[i] > max_num:
            max_num = nli[i]
        else:
            ans += (max_num-nli[i])

    print(ans)
