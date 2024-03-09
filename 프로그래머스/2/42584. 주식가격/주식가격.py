def solution(prices):
    answer = []
    
    for i in range(len(prices) - 1):
        now_num = prices[i]
        result = 0
        for j in range(i+1, len(prices)):
            if now_num <= prices[j]:
                result += 1
            elif now_num > prices[j]:
                result +=1
                break
        
        answer.append(result)
            
    answer.append(0)
    return answer