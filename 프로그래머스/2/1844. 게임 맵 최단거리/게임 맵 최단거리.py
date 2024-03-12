from collections import deque
def solution(maps):
    #방향정의
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    def bfs(x, y):
        queue = deque()
        queue.append((x,y))

        while queue:
            x, y = queue.popleft()

            #방향돌리기
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]

                #맵 안의 유효한 좌표인지 검증
                if nx < 0 or nx >= len(maps) or ny < 0 or ny >= len(maps[0]):
                    continue

                #벽인지 검증
                if maps[nx][ny] == 0:
                    continue

                #유효한 값일때
                if maps[nx][ny] == 1:
                    maps[nx][ny] = maps[x][y] + 1
                    queue.append((nx,ny)) #재귀
                
        return maps[len(maps)-1][len(maps[0])-1]
                
    
    answer = bfs(0,0)
    if answer == 1 :
        return -1
    
    return answer