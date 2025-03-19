n = int(input())
m = int(input())
INF = int(1e9)
graph = [[INF] * (n+1) for _ in range(n+1)]

#자기자신으로 가는 비용 0으로 초기화
for i in range(n+1):
    for j in range(n+1):
        if i == j :
            graph[i][j] = 0

#여러가지 노선 중 비용이 제일 작은 노선으로 집어넣기
for i in range(m):
    #a에서 b로 가는 비용 c
    a, b, c = map(int, input().split())
    if graph[a][b] > c:
        graph[a][b] = c

#플로이드 알고리즘
for k in range(n+1):
    for a in range(n+1):
        for b in range(n+1):
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])


for i in range(1, n+1):
    for j in range(1, n+1):
        if graph[i][j] != INF:
            print(graph[i][j], end = ' ')
        else:
            print(0, end = ' ')
    print()