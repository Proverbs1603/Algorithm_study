def solution(friends, gifts):
    # 선물 준 횟수
    give_gift_count = {person:0 for person in friends}
    # 선물 받은 횟수
    receive_gift_count = {person:0 for person in friends}
    #선물지수
    gift_idx = {}
    
    #준사람, 받은사람, 횟수 데이터 생성
    gift_matrix = dict()
    for i, person in enumerate(friends):
        gift_matrix[person] = {friends[j]: 0 for j in range(len(friends)) if person != friends[j]}
    
    #선물 계산해보기
    for gift in gifts:
        giver, receiver = gift.split(' ')
        give_gift_count[giver] += 1 
        receive_gift_count[receiver] += 1
        gift_matrix[giver][receiver] += 1
        
    #선물 지수 계산하기 
    #선물지수 = 준선물 - 받은선물
    gift_idx = {person : give_gift_count[person] - receive_gift_count[person] for person in friends}
    
    
    result = []    
    #선물 계산해보자
    for person in gift_matrix:
        
        #선물받은 횟수
        gift_num = 0
        comp_data = gift_matrix[person]
        for comp_person in comp_data:
            
            ##비교로직
            if gift_matrix[person][comp_person] > gift_matrix[comp_person][person]:
                gift_num += 1
            elif gift_matrix[person][comp_person] == gift_matrix[comp_person][person]:
                #같다면 선물지수 비교
                if gift_idx[person] > gift_idx[comp_person]:
                    gift_num += 1
        result.append((person, gift_num))
    
    #print(result)
    max_gift_num = max(result, key = lambda x:x[1])[1] 
    return max_gift_num