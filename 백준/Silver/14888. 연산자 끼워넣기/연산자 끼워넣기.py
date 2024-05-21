#백준 14888 문제
#예제 
# 2
# 5 6
# 0 0 1 0
from itertools import permutations
N = int(input())
data = list(map(int, input().split()))
op_list = ['+', '-', '*', '/']
num_operator = list(map(int, input().split()))
op = []

#연산자 갯수만큼 +, -, *, / 를 op리스트에 넣어주기
for k in range(len(num_operator)):
    for _ in range(num_operator[k]):
        op.append(op_list[k])

maximum = -1e9
minimum = 1e9

def solve():
    global maximum, minimum
    for case in permutations(op, N-1):
        total = data[0]
        for r in range(1,N):
            if case[r-1] == '+':
                total += data[r]
            elif case[r-1] == '-':
                total -= data[r]
            elif case[r-1] == '*':
                total *= data[r]
            elif case[r-1] == '/':
                total = int(total/data[r])
            
        maximum = max(total, maximum)
        minimum = min(total, minimum)

solve()
print(maximum)
print(minimum)
