def solution(array, commands):
    answer = []
    #1번째 슬라이싱
    #2번째 sorting
    #3번째 해당 위치의 숫자를 answer에 append
    # ->commands의 길이 만큼 반복
    
    for command in commands:
        #2,5가 들어온다
        #ex) array[1:5] -> [2,3,5,6]
        clist = array[command[0] - 1 : command[1]]
        list.sort(clist)
        answer.append(clist[command[2] - 1])
    
    return answer