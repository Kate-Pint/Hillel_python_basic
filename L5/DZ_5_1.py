import keyword
import string
my_word = '_'
#my_word = '__'
#my_word = '___'
#my_word = 'x'
#my_word = 'get_value'
#my_word = 'get value'
#my_word = 'get!value'
#my_word = 'some_super_puper_value'
#my_word = 'Get_value'
#my_word = 'get_Value'
#my_word = 'getValue'
#my_word = '3m'
#my_word = 'm3'
#my_word = 'assert'
#my_word = 'assert_exception'
print(my_word)
if my_word in keyword.kwlist:
    print(False)
elif my_word[0].isdigit():
    print(False)
elif any(char.isupper() for char in my_word):
    print(False)
elif any(char in " ".join(string.punctuation.split("_")) for char in my_word):
    print(False)
elif my_word.count("_") > 1 and my_word.count("_") == len(my_word):
    print(False)
else:
    print(True)

