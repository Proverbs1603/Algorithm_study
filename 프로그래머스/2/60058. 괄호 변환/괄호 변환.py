 #올바른 문자인지 확인
def isRight(s):
    stack = []
        
    for i in s:
        if i == '(':
                stack.append(i)
        else:
            if len(stack) == 0:
                return False
            stack.pop()
    return True

#u,v로 나누기
def divide(s):
    left, right = 0,0
    #분해과정은 u의 '(' 와 ')'의 개수가 맞을 때 분해되기
    for i in range(len(s)):
        if s[i] == '(':
            left += 1
        else:
            right += 1
            
        if left == right:
            return s[:i+1], s[i+1:]

def solution(p):
    if not p:
        return ''

    #p가 이미 올바른 괄호 문자열인지 확인하기
    if(isRight(p)):
        return p
    
    #p가 올바른 괄호 문자열이 아니라면 u와 v로 분해하기
    u, v = divide(p)
    
    #u가 올바른 괄호 문자열인지 확인
    if isRight(u):
        # 3-1. 수행한 결과 문자열을 u에 이어 붙인 후 반환합니다.
        return u + solution(v)
    #4. 문자열 u가 "올바른 괄호 문자열"이 아니라면 아래 과정을 수행합니다. 
    else:
        #4-1. 빈 문자열에 첫 번째 문자로 '('를 붙입니다.
        answer = '('
        #4-4. u의 첫 번째와 마지막 문자를 제거하고, 나머지 문자열의 괄호 방향을 뒤집어서 뒤에 붙입니다.
        answer += solution(v)
        #4-3. ')'를 다시 붙입니다.
        answer += ')'
        
        # 아니면 다음과 같이 새로운 문자열로 만들기 - u의 앞뒤 문자를 제거하고, 나머지 문자의 괄호 방향을 뒤집기
        for s in u[1:len(u)-1]:
            if s == '(':
                answer += ')'
            else:
                answer += '('
        return answer
