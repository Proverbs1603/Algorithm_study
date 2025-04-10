from itertools import permutations

def solution(k, dungeons):
    max_cnt = -1
    permu = list(permutations(dungeons))
    
    for per_list in permu:
        cnt = 0
        temp_k = k
        for dungeon in per_list:
            min_req_ticket = dungeon[0]
            req_ticket = dungeon[1]
            if temp_k >= min_req_ticket:
                temp_k -= req_ticket
                cnt += 1
                
        max_cnt = max(max_cnt, cnt)
    
    answer = max_cnt
    return answer