import itertools
def is_prime_number(x):
    if x == 1 :
        return False
    # 2부터 (x - 1)까지의 모든 수를 확인하며
    for i in range(2, x):
        # x가 해당 수로 나누어떨어진다면
        if x % i == 0:
            return False # 소수가 아님
    return True # 소수임

def solution(numbers):
    #리스트에 일단 숫자로 다 담기(문자열 리스트)
    num_string_list = []
    for number in numbers:
        num_string_list.append(number)
    
    
    num_list = []
    #숫자를 조합해서 만들어야함.
        
    for i in range(len(num_string_list)):
        num_list += list(map(''.join, itertools.permutations(num_string_list, i+1)))
    
    #실제 가능한 숫자만 포함한 리스트
    pos_num_set = set()
    
    for i in range(len(num_list)):
        if num_list[i].isdecimal() and num_list[i][0] != '0':
            pos_num_set.add(int(num_list[i]))
    
    print(pos_num_set)
    answer = 0    
    for num in pos_num_set :
        if is_prime_number(num):
            answer+=1

    return answer