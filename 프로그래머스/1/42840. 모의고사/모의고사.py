def solution(answers):
    answer_1 = [1,2,3,4,5]
    answer_2 = [2,1,2,3,2,4,2,5]
    answer_3 = [3,3,1,1,2,2,4,4,5,5]
    
    correct_list = [0,0,0]         
    for i, answer in enumerate(answers):
        if answer == answer_1[i%len(answer_1)]:
            correct_list[0] += 1
        if answer == answer_2[i%len(answer_2)]:
            correct_list[1] += 1
        if answer == answer_3[i%len(answer_3)]:
            correct_list[2] += 1
    
    result = []
    max_correct_count = max(correct_list)
    for i , correct_count in enumerate(correct_list, start=1):
        if correct_count == max_correct_count:
            result.append(i)
        
    return result