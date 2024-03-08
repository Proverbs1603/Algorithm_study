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
            
    for key, value in sorted(score.items(), key=lambda x:x[1], reverse=True):
        for i, play in sorted(index[key], key=lambda x:x[1], reverse=True)[:2]:
            answer.append(i)
            
    return answer