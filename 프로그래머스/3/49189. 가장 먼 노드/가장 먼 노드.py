from collections import deque
def solution(n, edge):
    graph = [[] for _ in range(n+1)]
    distance = [-1] * (n+1)
    
    #그래프 정보 추가
    for e in edge:
        graph[e[0]].append(e[1])
        graph[e[1]].append(e[0])
        
    #간선 1부터 시작해야하니 1을 가지고 있는 deque로 생성
    queue = deque([1])
    #출발 노드의 최단거리는 0 (방문처리도 맞음)
    distance[1] = 0
    
    while queue:
        #현재 방문하는 노드
        now = queue.popleft()
        
        #현재노드와 인접한 노드들 방문
        for i in graph[now]:
            #방문하지 않은 노드라면 큐에 방문할 노드로 추가
            if distance[i] == -1:
                queue.append(i)
                #현재 노드보다 +1 해주기
                distance[i] = distance[now] + 1
    #가장 멀리 떨어진 노드 갯수 세기
    answer = 0
    for i in range(len(distance)):
        if distance[i] == max(distance):
            answer += 1

    return answer