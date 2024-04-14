import heapq

N = int(input())
heap = []
for i in range(N):
    heapq.heappush(heap, int(input()))
    
result = 0
#각 원소 합 추가해두는 리스트
ls = []
#힙에 하나의 원소만 (덱)만 있을 때
while len(heap) != 1 :
    #가장 작은 수 2개 뽑아서 더하기
    num1 = heapq.heappop(heap)
    num2 = heapq.heappop(heap)
    sum1 = num1 + num2
        #결과에 추가하기
    result += sum1
    #그 결과를 힙에 다시 넣기
    heapq.heappush(heap,sum1)
    
    #각 결과를 추가해두는 리스트
    ls.append(sum1)


#결과를 저장한 리스트를 다 더해주면 답
answer = sum(ls)
print(answer)