from collections import deque
import copy

def solution(land):
    
    depth = len(land)    #깊이
    width = len(land[0]) #넓이  
    dx = [1, 0, 0, -1] #방향좌표
    dy = [0, 1, -1, 0] #방향좌표
    
    oil_list = [0 for _ in range(width)] #각 열의 석유량 리스트
    visited = [[False for _ in range(width)] for _ in range(depth)]  #방문 목록

    
    #시추하면 좌표를 1로 바꾸기
    #시추 발견시 bfs로 탐색하기
    #좌표 param으로 받기
    def drill(param_x, param_y):
    
        #획득 오일 
        oil_num = 1
        # 현재 위치는 시추했으므로 0으로 설정         
        visited[param_x][param_y] = True
        #큐 선언
        queue = deque()
        queue.append((param_x, param_y))
        
        # 석유가 존재하는 열 저장 (중복 방지)
        oil_covered = set()
        oil_covered.add(param_y)
        
        #bfs로 탐색
        while queue:
            #좌표뽑기
            x, y = queue.popleft()
            
            for i in range(4):
                now_x = x + dx[i]
                now_y = y + dy[i]
                
                #석유면 계속 탐색하고 노다지로 바꾸기
                if (0 <= now_x < depth) and (0 <= now_y < width) and visited[now_x][now_y] == False and land[now_x][now_y] == 1:
                    
                    oil_num += 1   #석유 1개 추가
                    queue.append((now_x, now_y)) #큐에 추가
                    visited[now_x][now_y] = True #방문 처리
                    oil_covered.add(now_y) #석유가 존재하는 열 저장
                    
        #print(f'oil_covered는 ({oil_covered})')
        #석유가 존재하는 열에 값을 더해주기
        for c in oil_covered:
            oil_list[c] += oil_num
        #print(oil_list)
        
        return
        
    #시추관 탐색하기 (위에서 아래방향으로)
    for col in range(width):
        for row in range(depth):
            #석유를 발견했고 방문하지 않은 곳일때
            if land[row][col] == 1 and not visited[row][col]: 
                #시추하기
                drill(row, col)

           
    answer = max(oil_list)
    return answer