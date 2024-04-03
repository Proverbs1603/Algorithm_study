S = input()

# 0 또는 1로 이루어진 그룹 개수 세기
numZeros = 1 if S[0] == '0' else 0
numOnes = 1 if S[0] == '1' else 0
result = 0

for i, num in enumerate(S[1:]):
    if num == '0' and S[i] != '0':
        numZeros += 1
        continue
    
    if num == '1' and S[i] != '1':
        numOnes += 1
            
if numZeros > numOnes:
    result = numOnes
else:
    result = numZeros
    
print(result)   