lst = [12, 3, 4, 10]
#lst = [1]
#lst = []
#lst = [12, 3, 4, 10, 8]
print(lst)
if len(lst) > 0:
    x = lst.pop()
    lst.insert(0, x)
    print(lst)
else:
    print(lst)
