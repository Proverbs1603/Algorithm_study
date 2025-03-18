word = list(input())[::-1]
count = 0
i = 0
#거꾸로 뒤집어서 확인하기
while i < len(word):
    if i + 1 < len(word) and word[i] == '-':
        if word[i+1] == 'd':
            del word[i:i+2]
            count += 1
            continue
            
    elif i + 1 < len(word) and word[i] == '=':
        if word[i+1] == 'c' or word[i+1] == 's':
            del word[i:i+2]
            count += 1
            continue
        elif word[i+1] == 'z':
            if i + 2 < len(word) and word[i+2] == 'd':
                del word[i:i+3]
                count += 1
                continue
            else:
                del word[i:i+2]
                count += 1
                continue
    elif i + 1 < len(word) and word[i] == 'j':
        if word[i+1] == 'n' or word[i+1] == 'l':
            del word[i:i+2]
            count += 1
            continue
        else:
            del word[i]
            count += 1
            continue
    else:
        del word[i]
        count += 1
        continue

    #삭제 안한 경우만 인덱스 증가시킴
    i += 1
print(count)
