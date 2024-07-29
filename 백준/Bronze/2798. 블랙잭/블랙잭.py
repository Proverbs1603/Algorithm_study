import sys
input = sys.stdin.readline
N, M = map(int, input().split())
data = list(map(int, input().split()))

result = 0
for i in range(0, N):
    for j in range(i+1, N):
        for k in range(j+1, N):
            temp_result = data[i] + data[j] + data[k]
            if (temp_result <= M) and (temp_result > result) :
                result = temp_result

print(result)