n, k = map(int, input().split())
circle = [i for i in range(0,n+1)]
result = []

#이터레이터 (포인터)
it = k
#7명이면 7번 반복해서 다 빼기
for i in range(n):
    #리스트 원소를 지운 다음에 이터레이터를 뒤로 옮기기

    result.append(circle[it])
    del circle[it]

    #리스트의 끝에서 삭제됐다면 이터레이터를 맨 앞으로 옮기기       
    if it == len(circle):
        it = 1
    
    #k-1번 뒤로 옮기기 (뒤 원소 있으면 옮기고 없으면 처음으로 초기화
    for j in range(k-1):
        new_it = it + 1
        if new_it <= len(circle)-1:  #배열을 1 크게 만들어서 -1하고 작은지 판단
            it = new_it
        else:
            it = 1

output = '<'
for idx, r in enumerate(result):
    if idx == len(result) - 1 :
        output += str(r)
    else:
        output += str(r) + ', '
else:
    output += '>'
print(output)