n = int(input())

dp = [-1] * (5001)

dp[3] = 1
dp[5] = 1

# 값이 5이하로 들어오면 그냥 출력
if n <= 5:
    print(dp[n])
else:
    #dp[6] 부터 dp[n] 까지 계산
    for i in range(6, n+1):
        #만약에 3번째 전이 -1 이 아니라면 +1 값을 넣어준다
        b3 = dp[i-3]
        b5 = dp[i-5]

        # 여러가지 경우의 수가 있는데 3번째 전과 5번째 전 둘 다 존재하면 min쓰기
        # 둘 중 하나만 존재하면 하나값만 넣어주기
        # 둘 다 존재 안하면 -1 으로 pass

        if b3 == -1 and b5 != -1:
            dp[i] = b5 + 1
        elif b3 != -1 and b5 == -1:
            dp[i] = b3 + 1
        elif b3 != -1 and b5 != -1:
            dp[i] = min(b3 + 1, b5 + 1)
        else:
            pass
    print(dp[n])
