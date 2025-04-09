def solution(tickets):
    dic = {ticket[0]: [] for ticket in tickets}
    
    for ticket in tickets:
        start = ticket[0]
        end = ticket[1]
        dic[start] += [end]
        
    for key in dic:
        dic[key].sort(reverse=True)
    
    answer = []
    
    def dfs(node):
        # 맨 끝에 아니고 또 value가 있을 때
        while node in dic and dic[node]:
            next_node = dic[node].pop()
            dfs(next_node)
        answer.append(node)
    
    dfs("ICN")
    
    return answer[::-1]