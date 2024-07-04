cust_number = int(input('Type five-digit number: '))
a = cust_number % 10
b = (cust_number % 100) // 10
c = (cust_number // 100) % 10
d = (cust_number // 1000) % 10
e = cust_number // 10000
reversed_number = a * 10000 + b * 1000 + c * 100 + d * 10 + e
print(reversed_number)