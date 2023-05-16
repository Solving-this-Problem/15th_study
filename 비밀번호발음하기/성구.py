# 4659 주식 bf
import sys
input = sys.stdin.readline

def isPronounced(word):
    # 연속 모음 개수,연속 자음 개수, 총 모음 개수
    moem_cnt = jaem_cnt = total_moem = 0
    for idx in range(len(word)):
        # 모음일 때
        if word[idx] in moem:
            moem_cnt += 1
            jaem_cnt = 0
            total_moem += 1
        # 자음일 때
        else:
            moem_cnt = 0
            jaem_cnt += 1
        # 연속으로 3개나오면 컷
        if moem_cnt >= 3 or jaem_cnt >= 3:
            # print(1)
            return 0
        # 두개여도 같은 글자가 나오면 컷!(ee, oo 제외)
        if (moem_cnt == 2 or jaem_cnt == 2) and word[idx] == word[idx-1] and word[idx] not in ['e', 'o']:
            # print(3)
            return 0
    # 모음이 하나도 없어도 컷!
    if not total_moem:
        # print(2)
        return 0
    return 1

# 모음 모음집
moem = ['a', 'e', 'i', 'o', 'u']
while True:
    password = input().strip()
    # end 글자가 나올 때까지 반복
    if password == 'end':
        break
    if isPronounced(password):  # 비밀번호가 조건에 만족
        print(f'<{password}> is acceptable.')
    else:       # 비밀번호 조건에 불만족
        print(f'<{password}> is not acceptable.')