import heapq

def make_new_food(a, b):
    return a + b * 2

def solution(scoville, K):
    answer = 0
    #리스트를 우선순위 큐로 바꾸기
    heapq.heapify(scoville)
    
    #작은거를 2개 빼서 만들기 until 모든 list원소가 K보다 같거나 크게
    while len(scoville) > 1:
        
        #가장 맵지 않은 음식이 K 이상이면 종료
        if scoville[0] >= K:
            break
            
        min1 = heapq.heappop(scoville)
        min2 = heapq.heappop(scoville)
        new_food = make_new_food(min1, min2)
        heapq.heappush(scoville,new_food)
        answer += 1
    
    
    if len(scoville) == 1 and scoville[0] < K:
        return -1
    
    return answer

