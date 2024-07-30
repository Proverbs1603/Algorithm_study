word = input()
upper_word = word.upper()

data = {}
for chr in upper_word:
    if chr not in data:
        chr_num = upper_word.count(chr)
        data[chr] = chr_num
    
max_result = max(data, key =data.get)

max_value = data[max_result]


data_list = list(data.values())

# print(data_list)
cnt = 0
for num in data_list:
    if num == max_value:
        cnt += 1

if cnt >= 2:
    print('?')
else:
    print(max_result)



