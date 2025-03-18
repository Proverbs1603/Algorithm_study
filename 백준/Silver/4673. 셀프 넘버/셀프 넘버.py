def dn(num):
    nums = sum(list((map(int, list(str(num))))))
    return num + nums

i = 1
s = set()
while i > 0:
    number = dn(i)
    if number >= 10000:
        break
    else:
        s.add(number)
    i += 1

    

for i in range(1,9994):
    if i not in s:
        print(i)
