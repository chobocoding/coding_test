input_num = int(input())
num_count = 0

for i in range(1, input_num+1):
    num_list = [input_num, i]
    while (num_list[-1] >= 0):
        num_list.append(num_list[-2] - num_list[-1])
    num_list.pop(-1)
    if num_count < len(num_list):
        max_num_list = num_list
        num_count = len(num_list)
print(num_count)
print(*max_num_list)
