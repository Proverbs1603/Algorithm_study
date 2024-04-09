from collections import deque

N = int(input())

#NxN 정사각 보드
arr = [[0]*N for _ in range(N)]

#맵에 사과표시
K = int(input())
for i in range(K):
    row, col = map(int,input().split())
    arr[row-1][col-1] = 1

#방향전환 횟수 입력받기
L = int(input())
time_dic = {}
for i in range(L):
    X, C = input().split()
    time_dic[int(X)] = C

#상우하좌 #90도로 뱀이 회전해야해서 시계방향 순서대로 차례대로 놓아야함.
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

#뱀 초기위치, 방향 초기
x, y, d = 0, 0, 0

#뱀
snake = deque([])
time = 0

while True:
    #뱀머리 현재위치
    snake.append((x,y))
    time += 1

    #보고있는 방향으로 전진
    x += dx[d]
    y += dy[d]
    
    #벽에 부딪히거나 자기 몸과 부딪히면
    if x < 0 or x >= N or y < 0 or y >= N or arr[x][y] == 2:
        break
    
    #벽이 아니면 
    #사과가 없다면 arr[x][y] == 0 이라면
    if not arr[x][y]:
        #꼬리를 없애준다
        i, j = snake.popleft()
        arr[i][j] = 0

    #뱀이 지나간 자리이므로 2로 설정해둠
    arr[x][y] = 2

    #방향전환 시간이 되었을때
    if time in time_dic:
        if time_dic[time] == 'D':
            d = (d + 1) % 4
        else:
            d = (d - 1) % 4

print(time)
