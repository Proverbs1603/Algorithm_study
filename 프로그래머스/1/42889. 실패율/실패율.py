def solution(N, stages):
    result = []
    #전체 사용자
    total_num = len(stages)
    for i in range(1,N+1):
        #현재 스테이지에 머물러있는 숫자
        count = stages.count(i)
        
        #실패율 계산
        failure_rate = count / total_num if total_num > 0 else 0
        
        #사용자 감소
        total_num -= count

        #스테이지랑 결과 같이 저장
        result.append((i,failure_rate))

    #내림차순 정렬
    result.sort(key=lambda x : -x[1])
    answer = [res[0] for res in result]
        
    return answer
