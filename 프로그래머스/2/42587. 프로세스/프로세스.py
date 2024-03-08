def solution(priorities, location):
    answer_list = []
    
    #처음에 꼬리표 달아놓기
    priorities = [(idx,priority) for idx, priority in enumerate(priorities)]
    
    
    while priorities:
        has_priority = True
        #tuple 하나 빼기
        tuple_priority = priorities.pop(0)
        
        #순회하면서 비교하기
        for i in range(len(priorities)):
            if tuple_priority[1] < priorities[i][1]:
                priorities.append(tuple_priority)
                has_priority = False
                break;
        
        if has_priority:
            answer_list.append(tuple_priority)
        
    #location 위치 찾기     
    for i in range(len(answer_list)):
        if answer_list[i][0] == location:
            answer = i + 1
    return answer