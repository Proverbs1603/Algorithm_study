import sys
input = sys.stdin.readline
N = int(input())
t = [] #상담기간
p = [] #금액
dp = [0] * (N+1) #dp array

max_value = 0

for i in range(N):
    x, y = map(int,input().split())
    t.append(x)
    p.append(y)

for k in range(N-1, -1, -1):
    time = k + t[k]
    if time <= N:
        dp[k] = max(p[k] + dp[k+t[k]], max_value)
        max_value = dp[k]
    else:
        dp[k] = max_value

print(max_value)