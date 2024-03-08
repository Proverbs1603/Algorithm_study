def solution(nums):
    answer = len(nums) / 2
    dic = dict()
    for item in nums:
        if item in dic:  # 이미 딕셔너리에 키가 있는지 확인
            dic[item] += 1
        else:
            dic[item] = 1
    if answer > len(dic):
        answer = len(dic)
    
    return answer