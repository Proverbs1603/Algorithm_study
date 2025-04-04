def solution(n, computers):
    # 탐색하면서 방문 체크하기
    def dfs(x, y):
        # 방문처리
        computers[x][y] = 0
        # 컴퓨터 노드 돌면서 방문체크하고 재귀
        for node in range(n):
            # 다른 노드로만 탐색
            if x != node:
                if computers[x][node] == 1:
                    computers[x][node] = 0
                    dfs(node, node)


        
            

                
    answer = 0
    # 1번부터 ~ n번까지 dfs 해서 반환되면 1씩 더하기
    for i in range(n):
        if computers[i][i] != 0:
            dfs(i, i)
            answer += 1
            
    return answer