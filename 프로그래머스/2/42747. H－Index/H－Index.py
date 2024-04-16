def solution(citations):
    citations.sort(reverse=True)
    h_index_list = []
    for i in range(len(citations)):
        if i+1 < citations[i]:
            h_index_list.append(i+1)
        else:
            h_index_list.append(citations[i])
    
    answer = max(h_index_list)
    return answer