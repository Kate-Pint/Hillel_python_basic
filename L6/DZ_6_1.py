import string
value = "a-A"
# value = "a-c"
# value = "a-a"
# value = "s-H"
lst = string.ascii_letters
first_value = value.split("-")[0]
second_value = value.split("-")[1]
print(lst[lst.index(first_value):lst.index(second_value)+1])