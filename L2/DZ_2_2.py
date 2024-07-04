cust_number = int(input('Type five-digit number: '))
a = cust_number % 10
b = (cust_number % 100) // 10
c = (cust_number // 100) % 10
d = (cust_number // 1000) % 10
e = cust_number // 10000
print(str(a)+str(b)+str(c)+str(d)+str(e))