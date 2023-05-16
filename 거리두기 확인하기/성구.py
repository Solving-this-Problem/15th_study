# 프로그래머스 - 거리두기 확인하기 bf
def check(y, x, arr):
    #아래로 2칸 확인
    for i in range(3):
        # 피라미드 모양으로 확인
        for j in range(abs(i)-2, 3-abs(i)):
            # 만약 주변에 P가 있다면
            if 0<=y + i < 5 and 0<= x+j < 5 and  arr[y+i][x+j] == 'P':
                # 맨허튼 거리가 1일땐 무조건 거리두기 실패
                if abs(i) + abs(j) == 1:
                    print(y,x, 1)
                    return 1
                # 같은 행에 있을 때 사이에 칸막이 없으면 실패
                if i == 0 and j != 0 and arr[y][x+j//2] != 'X':
                    print(y,x, 2)
                    return 1
                # 같은 열에 있을 때 사이에 칸막이 없으면 실패
                if i != 0 and j == 0 and arr[y+i//2][x] != 'X':
                    print(y,x, 3)
                    return 1
                # 대각선에 있을 때 
                if i != 0 and j != 0:
                    # 같은 열에 X가 없으면 안됌
                    if arr[y+1][x] != 'X':
                        print(y, x, 6)
                        return 1
                    else:
                        # 있어도 같은 행, P가 있는 쪽에 칸막이가 하나 더 있어야 함
                        # 좌측
                        if j<0 and arr[y][x-1] != 'X':
                            print(y, x, 4)
                            return 1
                        # 우측
                        elif j>0 and arr[y][x+1] != 'X':
                            print(y, x, 5)
                            return 1

def solution(places):
    answer = []
    # 5개에 케이스에 대해 모두 확인
    for room in range(5):
        print('page', room+1)
        i= j = 0
        while i< 5 and j <5:
            # 시작점 찾기
            if places[room][i][j] == 'P':
                # 거리두기 안 한 사람이 있으면 바로 컷!
                if check(i, j, places[room]):
                    answer.append(0)
                    break
            if j <4:
                j += 1
            elif j == 4:
                i += 1
                j = 0   
        else:   # 모두 통과하면 1추가
            answer.append(1)
        print()
    return answer