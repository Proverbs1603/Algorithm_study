import sys
from itertools import combinations
input = sys.stdin.readline
N, C = map(int, input().split())
data = []
for i in range(N):
    data.append(int(input()))
data.sort()

#공유기 최소거리
start = 1
#공유기 최대거리
end = data[-1] - data[0]
result = 0

while start <= end:
    mid = (start + end) // 2
    current = data[0]
    count = 1

    #공유기 몇 대 설치 가능한지
    for i in range(1, len(data)):
        if data[i] - current >= mid:
            count += 1
            current = data[i]
    
    #공유기 설치 수가 목표 수 보다 크면 공유기 사이 거리 늘림
    if count >= C:
        start = mid + 1
        result = mid
    #공유기 설치 수가 목표 수 보다 작으면 공유기 사이 거리 줄임
    else:
        end = mid - 1
print(result)

