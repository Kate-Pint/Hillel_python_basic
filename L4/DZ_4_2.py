lst = [1, 3, 5]
if len(lst) == 0:
    print(sum(lst))
else:
    i_last_num = int(len(lst)-1)
    new_list = [i for i in lst[0::2]]
    print(sum(new_list) * lst[i_last_num])
