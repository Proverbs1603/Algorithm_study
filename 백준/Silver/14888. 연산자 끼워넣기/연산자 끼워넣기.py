N = int(input())
numbers = list(map(int, input().split()))

add, minus, multi, div = map(int, input().split())

# dfs를 활용한 완전탐색
min_value = 1e9 + 1
max_value = -1e9 - 1

def dfs(value, depth):
    global add, minus, multi, div, min_value, max_value
    
    if depth == N:    
        min_value = min(min_value, value)
        max_value = max(max_value, value)
    else:
        
        if add > 0:
            add -= 1
            dfs(value+numbers[depth], depth+1)
            add += 1
        
        if minus > 0:
            minus -= 1
            dfs(value-numbers[depth], depth+1)
            minus += 1
        
        if multi > 0:
            multi -= 1
            dfs(value*numbers[depth], depth+1)
            multi += 1
        
        # 음수를 양수로 나눌 때는 C++14의 기준을 따른다. 즉, 양수로 바꾼 뒤 몫을 취하고, 그 몫을 음수로 바꾼 것과 같다. 이에 따라서, 위의 식 4개의 결과를 계산해보면 아래와 같다.
        if div > 0:
            div -= 1
            if value < 0:
                new_value = -(-value // numbers[depth])
            else:
                new_value = value // numbers[depth]
            dfs(new_value, depth+1)
            div += 1

dfs(numbers[0], 1)
print(max_value)
print(min_value)