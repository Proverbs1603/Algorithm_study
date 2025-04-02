from collections import deque

n, m = map(int, input().split())
graph = [list(map(int, list(input()))) for _ in range(n)]

# visited[x][y][0]: (x, y)에 찬스를 안 쓰고 도달한 경우
# visited[x][y][1]: (x, y)에 찬스를 쓰고 도달한 경우
visited = [[[False]*2 for _ in range(m)] for _ in range(n)]

dx = [1, -1, 0, 0]
dy = [0, 0, -1, 1]

def bfs():
    queue = deque()
    queue.append((0, 0, 0, 1))  # x, y, chance_used(0/1), distance
    visited[0][0][0] = True

    while queue:
        x, y, chance, dist = queue.popleft()

        if x == n - 1 and y == m - 1:
            return dist

        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]

            if 0 <= nx < n and 0 <= ny < m:
                # 벽이 아닌 곳, 현재 찬스 사용 여부 그대로
                if graph[nx][ny] == 0 and not visited[nx][ny][chance]:
                    visited[nx][ny][chance] = True
                    queue.append((nx, ny, chance, dist + 1))

                # 벽인데 찬스를 아직 안 쓴 경우 → 부수고 감
                elif graph[nx][ny] == 1 and chance == 0 and not visited[nx][ny][1]:
                    visited[nx][ny][1] = True
                    queue.append((nx, ny, 1, dist + 1))

    return -1  # 도달 불가능

print(bfs())
