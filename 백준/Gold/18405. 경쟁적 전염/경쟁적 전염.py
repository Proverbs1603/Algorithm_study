from collections import deque
import sys
input = sys.stdin.readline
N, K = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(N)]
S, X, Y = map(int, input().split())
virus = []
for i in range(N):
    for j in range(N):
        if graph[i][j] != 0 :
            virus.append((graph[i][j], i, j))
virus.sort()

#상하좌우
d = [(-1,0), (1,0), (0,-1), (0,1)]

def bfs(s, X, Y):
    queue = deque(virus)
    count = 0
    while queue:
        if count == s:
            break
        for _ in range(len(queue)):
            prev, x, y = queue.popleft()
            for i in range(4):
                nx = x + d[i][0]
                ny = y + d[i][1]
                if (0<=nx<N) and (0<=ny<N):
                    if graph[nx][ny] == 0:
                        graph[nx][ny] = graph[x][y]
                        queue.append((graph[nx][ny], nx, ny))
        count+=1
    return graph[X-1][Y-1]

print(bfs(S,X,Y))
