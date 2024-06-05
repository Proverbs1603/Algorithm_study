import sys
input = sys.stdin.readline
n = int(input())
#정수삼각형 넣기
dp = [list(map(int, input().split())) for _ in range(n)]

#점화식 dp[i][j] += max(dp[i-1][j-1], dp[i-1][j])
for i in range(1,n):
    for j in range(len(dp[i])):
        #맨 처음인 경우 오른쪽만 고려하기
        if j == 0:
            dp[i][j] += dp[i-1][j]
        #맨 끝 쪽인 경우 왼쪽만 고려하기
        elif j == len(dp[i])-1:
            dp[i][j] += dp[i-1][j-1]
        #중간인 경우 양쪽 고려
        else:
            dp[i][j] += max(dp[i-1][j-1], dp[i-1][j])            

print(max(dp[n-1]))