def solution(genres, plays):
    index = {}
    score = {}
    answer = []
    
    for i, (genre, play) in enumerate(zip(genres, plays)):
        if genre in index:
            index[genre] += [(i,play)]
        else:
            index[genre] = [(i,play)]
        
        if genre in score:
            score[genre] += play
        else:
            score[genre] = play
            
    #items()로 꺼내야 sorted 할 때 정렬이 제대로 됨.
    #첫번째 정렬에서 score 딕셔너릴 정렬하여 장르별로 plays가 많은 순으로 정렬
    #두번째 정렬에서 index 딕셔너릴 정렬하여 장르안의 paly가 많은 순으로 정렬
    #고유번호 낮은 노래... 
    for key, value in sorted(score.items(), key=lambda x:x[1], reverse=True):
        for i, play in sorted(index[key], key=lambda x:x[1], reverse=True)[:2]:
            answer.append(i)
            
    return answer
