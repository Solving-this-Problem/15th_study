# 1987 알파벳 - DFS
# 아래와 같은 방식, list대신 set 사용하기
import sys
input = sys.stdin.readline

R, C = map(int, input().split())
board = [input().strip() for _ in range(R)]

stack = set([(0, 0, board[0][0])])
maxLen = 0

dir = [(0,1), (1,0), (-1,0), (0, -1)]
while stack:
    i, j, visited = stack.pop()

    if maxLen < len(visited):
        maxLen = len(visited)
        if maxLen == 26 or maxLen == R*C:
            break
    
    for di, dj in dir:
        ni, nj = i+di, j+dj
        if 0<=ni<R and 0<=nj<C and not board[ni][nj] in visited:
            stack.add((ni, nj, visited+board[ni][nj]))
print(maxLen)

''' DFS 방식 - pypy만 가능 3.896초 116168KB
import sys
input = sys.stdin.readline

R, C = map(int, input().split())
board = [input().strip() for _ in range(R)]

stack = [(0, 0, board[0][0])]
maxLen = 0

dir = [(0,1), (1,0), (-1,0), (0, -1)]
while stack:
    i, j, visited = stack.pop()

    if maxLen < len(visited):
        maxLen = len(visited)
        # 만약 최대가 되면 그만 해도 됨
        if maxLen == 26 or maxLen == R*C:
            break
    
    for di, dj in dir:
        ni, nj = i+di, j+dj
        if 0<=ni<R and 0<=nj<C and not board[ni][nj] in visited:
            stack.append((ni, nj, visited+board[ni][nj]))
print(maxLen)
'''
