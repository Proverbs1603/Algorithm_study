import sys
from collections import deque
input = sys.stdin.readline
#첫째 줄에 도시의 개수 N, 도로의 개수 M, 거리 정보 K, 출발 도시의 번호 X가 주어진다
N, M, K, X = map(int, input().split())
#그래프
graph = [[] for _ in range(N+1)]
queue = deque()
#방문처리 #거리
visited = set()
distances = [0]*(N+1)
#그래프에 데이터 넣기
for i in range(M):
    start, end = map(int, input().split())
    graph[start].append(end)  

#출발지 큐에 넣고 방문처리
queue.append(X)
visited.add(X)

while queue:
    #큐에서 노드 하나 꺼냄
    node = queue.popleft()
    #꺼낸 노드에서 가려는 노드를 하나씩 꺼내봄
    for next in graph[node]:
        #방문하지 않은 노드이면
        if next not in visited:
            #큐 맨 뒤에 넣고 방문처리
            queue.append(next)
            visited.add(next)
            #거리는 현재 노드에서 + 1
            distances[next] = distances[node] + 1

#거리에 K라는 값이 있으면 거리 저장한 정보 다 꺼내서 가는데 K만큼 걸린 목적지 다 출력
if K in distances:
    for destination in range(1,N+1):
        if distances[destination] == K:
            print(destination)
else:
    #없으면 -1 출력
    print(-1)