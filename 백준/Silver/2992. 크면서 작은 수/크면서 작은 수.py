str_num = input()
int_num = int(str_num)

data = list(str_num)
# print(data)

cnt = 0 
while True:
    if len(str(int_num)) != len(str_num):
        print(0)
        break

    int_num += 1
    list_temp_num = list(str(int_num))
    if sorted(list_temp_num) == sorted(data):
        print(int_num)
        break
    

    

    