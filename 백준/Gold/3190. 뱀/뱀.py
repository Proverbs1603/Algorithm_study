from collections import deque
#N 입력받고 맵 그리기
N = int(input())
arr = [[0]*N for _ in range(N)]

#사과 개수 입력받고 맵에 그려놓기
K = int(input())
for _ in range(K):
    x, y = map(int, input().split())
    arr[x-1][y-1] = 1

#뱀의 방향횟수 입력받고 dic에 저장해두기
L = int(input())
time_dic = {}
for i in range(L):
    X, C = input().split()
    time_dic[int(X)] = C
 
#상우하좌 #90도로 뱀이 회전해야해서 시계방향 순서대로 차례대로 놓아야함.
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

#뱀 초기 위치 #방향 초기화
x, y, d = 0, 0, 0

#뱀, 시간
snake = deque([])
time = 0 

while True:
    #뱀머리 현재위치
    snake.append((x, y))
    #시간증가
    time += 1
    #보고있는 방향으로 전진
    x += dx[d]
    y += dy[d]
    
    #만약 벽이나 자기자신의 몸과 부딪히면 게임이 끝난다.
    if  x < 0 or x >= N or y < 0 or y >= N or arr[x][y] == 2:
        break
    
    #벽이 아니면 
    #사과가 없다면 arr[x][y] == 0 이라면 꼬리를 없애주기
    #이동한 칸에 사과가 없다면, 몸길이를 줄여서 꼬리가 위치한 칸을 비워준다. 즉, 몸길이는 변하지 않는다.
    if not arr[x][y]:
        i, j = snake.popleft()
        arr[i][j] = 0
        
    #뱀의 몸을 2로 세이브
    arr[x][y] = 2
    
    #방향전환
    if time in time_dic:
        if time_dic[time] == 'D':
            d = (d + 1) % 4
        else:
            d = (d - 1) % 4
            
print(time)   