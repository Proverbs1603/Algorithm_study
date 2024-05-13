#첫째 줄에 자연수 N, K가 공백을 기준으로 구분되어 주어진다.
# (1 ≤ N ≤ 200, 1 ≤ K ≤ 1,000) 둘째 줄부터 N개의 줄에 걸쳐서 시험관의 정보가 주어진다.
#각 행은 N개의 원소로 구성되며, 
#해당 위치에 존재하는 바이러스의 번호가 공백을 기준으로 구분되어 주어진다. 
#단, 해당 위치에 바이러스가 존재하지 않는 경우 0이 주어진다.
 #또한 모든 바이러스의 번호는 K이하의 자연수로만 주어진다. N+2번째 줄에는 S, X, Y가 공백을 기준으로 구분되어 주어진다. (0 ≤ S ≤ 10,000, 1 ≤ X, Y ≤ N)
#S초 뒤에 (X,Y)에 존재하는 바이러스의 종류를 출력한다. 만약 S초 뒤에 해당 위치에 바이러스가 존재하지 않는다면, 0을 출력한다.

import sys
from collections import deque

input = sys.stdin.readline


#K는 바이러스 개수
N, K = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(N)]
virus = []
for i in range(N):
  for j in range(N):
    if graph[i][j] != 0:
      virus.append(((graph[i][j], i, j)))
virus.sort()
S, X, Y = map(int, input().split())

#상하좌우
d = [(-1,0), (1,0), (0,-1), (0,1)]
#bfs
def bfs(s, X, Y):
  queue = deque(virus)
  count = 0
  while queue:
    #while문 도는 횟수가 s초 지나는 거
    if count == s:
      break
    #바이러스 1,2,3... 한번씩 다 돌기
    for _ in range(len(queue)):
      prev, x, y = queue.popleft()
      for i in range(4):
        nx = x + d[i][0]
        ny = y + d[i][1]
        if 0 <= nx < N and 0 <= ny < N:
          if graph[nx][ny] == 0:
            graph[nx][ny] = graph[x][y]
            queue.append((graph[nx][ny], nx, ny))
    count += 1
  return graph[X-1][Y-1]

print(bfs(S,X,Y))