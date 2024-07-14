#first_list = [0, 1, 0, 12, 3]
#first_list = [0]
first_list = [1, 0, 13, 0, 0, 0, 5]
#first_list = [9, 0, 7, 31, 0, 45, 0, 45, 0, 45, 0, 0, 96, 0]
count_of_zero = first_list.count(0)
while 0 in first_list:
    first_list.remove(0)
zero_lst = [0]
print(first_list + zero_lst * count_of_zero)

