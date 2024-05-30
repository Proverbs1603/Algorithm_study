from bisect import bisect_left, bisect_right
def solution(words, queries):
    answer = []

    #같은 길이의 단어끼리 모으기
    w = [[] for _ in range(10001)]
    reverse_w = [[] for _ in range(10001)]
    for word in words:
        w[len(word)].append(word)
        reverse_w[len(word)].append(word[::-1])

    #정렬
    for i in range(10001):
        w[i].sort()
        reverse_w[i].sort()

    for q in queries:
        #이분탐색을 통해 범위 구하기
        # froaa <= for?? <= frozz
        # ????o 같은 접두사는 뒤집은걸로 구하기 oaaaa <= o???? <= ozzzz            
        qA = q.replace('?', 'a')
        qZ = q.replace('?', 'z')

        # ?가 접두사에 있는가? -> 단어를 뒤집어서 범위 구하기
        if q[0] == '?':
            s = bisect_left(reverse_w[len(q)], qA[::-1])
            e = bisect_right(reverse_w[len(q)], qZ[::-1])
            answer.append(e-s)
        else:
            #?가 접미사에 있다면
            s = bisect_left(w[len(q)], qA)
            e = bisect_left(w[len(q)], qZ)
            answer.append(e-s)
    return answer