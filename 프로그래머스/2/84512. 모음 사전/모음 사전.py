from itertools import product
def solution(word):
    words = []
    
    # A, E, I, O, U
    for i in range(1, 6):
        comb = list(product('AEIOU', repeat=i))
        for com in comb:
            words.append(''.join(com))

    words.sort()
    answer = words.index(word) + 1
    return answer