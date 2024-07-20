import string
text = input('Type your phrase: ')
new_text = ''.join([char for char in text.title() if char not in string.punctuation and char != ' '])
print("#" + new_text[:139])