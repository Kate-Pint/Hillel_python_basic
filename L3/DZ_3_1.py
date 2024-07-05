value_1 = int(input('Type first value: '))
operator = input('Type operator (*,/,+,-): ')
value_2 = int(input('Type second value: '))
if operator == '*':
    print(value_1 * value_2)
elif operator == '/' and value_2 > 0:
    print(value_1 / value_2)
elif operator == '/' and value_2 == 0:
    print('Divisor cannot equal "0"')
elif operator == '+':
    print(value_1+value_2)
elif operator == '-':
    print(value_1 - value_2)
else:
    print('Try again')
