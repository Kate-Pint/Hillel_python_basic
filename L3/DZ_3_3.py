lst = [1, 2, 3, 4, 5, 6]
#lst = [1, 2, 3]
#lst = [1, 2, 3, 4, 5]
#lst = [1]
#lst = []

is_odd = len(lst) % 2
if len(lst)>1 and is_odd > 0:
    lst[0] = lst[0:len(lst) // 2 + 1]
    lst[1] = lst[len(lst) // 2 + 1:]
    print(lst[0:2])
elif len(lst) > 1 and is_odd == 0:
    lst[0] = lst[0:len(lst) // 2]
    lst[1] = lst[len(lst) // 2:]
    print(lst[0:2])
elif len(lst) < 2:
    lst[:] = [lst[:1], lst[:-1]]
    print(lst)
else:
    print("Error")