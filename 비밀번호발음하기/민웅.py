import sys

vowel = ['a', 'e', 'i', 'u', 'o']
ex = ['e', 'o']

while True:
    word = input().strip()
    if word == 'end':
        break

    vowel_cnt = 0
    cnt = 0
    now = word[0]
    vowel_check = True
    if word[0] in vowel:
        vowel_cnt += 1
        cnt += 1
    else:
        vowel_check = False
        cnt += 1

    if len(word) > 1:
        for i in range(1, len(word)):
            if word[i] in vowel:
                vowel_cnt += 1
                if vowel_check:
                    cnt += 1
                else:
                    vowel_check = True
                    cnt = 1
            else:
                if vowel_check:
                    vowel_check = False
                    cnt = 1
                else:
                    cnt += 1
            if word[i] == word[i - 1]:
                if word[i] not in ex:
                    print(f'<{word}> is not acceptable.')
                    break

            if cnt >= 3:
                print(f'<{word}> is not acceptable.')
                break
        else:
            if vowel_cnt == 0:
                print(f'<{word}> is not acceptable.')
            else:
                print(f'<{word}> is acceptable.')
    else:
        if vowel_cnt == 0:
            print(f'<{word}> is not acceptable.')
        else:
            print(f'<{word}> is acceptable.')
