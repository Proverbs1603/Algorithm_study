def solution(phone_book):
    answer = True
    phone_book.sort()  # 전화번호를 사전순으로 정렬하여 접두어 관계를 쉽게 확인할 수 있도록 함
    for i in range(len(phone_book)):
        if i == len(phone_book) - 1 :
            break;
        if phone_book[i+1].startswith(phone_book[i]):
            answer = False
            return answer
    return answer
