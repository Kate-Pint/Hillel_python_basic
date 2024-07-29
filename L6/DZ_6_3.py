number = int(input("Type a number: "))
while number > 9:
    i = 1
    while number > 0:
        digit = number % 10
        i *= digit
        number //= 10
    number = i
print(number)