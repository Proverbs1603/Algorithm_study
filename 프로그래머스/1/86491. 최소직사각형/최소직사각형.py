def solution(sizes):
    #제일 큰 애를 일단 하나 뽑고 (필수)
    #제일 큰 애랑 그 size에서 큰 애를 뽑아서 비교하고 
    #작은애들끼리 비교해서 가장 큰 애를 고르면 됨.
    max_size = 0
    #가장큰 수 구하기
    for size in sizes:
        if size[0] >= max_size:
            max_size = size[0]
        if size[1] >= max_size:
            max_size = size[1]
    
    max_size_in_small_num = 0
    #작은 수들끼리 비교해서 제일 큰 애 구하기    
    for size in sizes:
        internal_min_num = min(size)
        if internal_min_num >= max_size_in_small_num:
            max_size_in_small_num = internal_min_num

        
    answer = max_size * max_size_in_small_num 
    return answer