N = int(input())
num = str(N)
size = len(num)
half_1 = 0
half_2 = 0
for i in range(size):
    if i < size//2:
        half_1 += int(num[i])
    else:
        half_2 += int(num[i])
        
print("LUCKY") if half_1 == half_2 else print("READY")

