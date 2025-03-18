n = int(input())

count = 0
for i in range(n):
    word = input()
    # word가 한글자라면 그룹단어니까 count증가시키고 스킵
    if len(word) == 1:
        count += 1
        continue

    #한글자 아니면 순회
    word_list = list(word)
    #해당 문자열 셌었는지 확인하는 집합 선언
    s = set()

    for idx, letter in enumerate(word_list):
        #만약 해당 문자열이 첫번째 순서가 아니고 이미 확인된 집합이라면 뒤에 문자열과 같은지 확인해봐야함
        if idx != 0 and letter in s:
            #같으면 계속해서 진행하고 같지 않으면 그룹단어가 아니므로 확인 그만하기
            if word_list[idx] != word_list[idx-1]:
                break
        #마지막에 집합에 저장하기
        s.add(letter)
    else:
        #다 통과하면 그룹단어이므로 카운트 증가
        count += 1       
print(count)