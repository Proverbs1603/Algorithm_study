def solution(s):
    answer = True
    stack = []

    for i in range(len(s)):
        if s[0] == ')':
            answer = False
            break
        
        if s[i] == '(':
            stack.append(s[i])
        elif '(' in stack and s[i] == ')':
            stack.pop()
    
    if len(stack) != 0 :
        answer = False

    return answer
