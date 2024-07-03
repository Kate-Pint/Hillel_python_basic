cust_number = int(input('Type five-digit number: '))
print((cust_number % 10), ((cust_number % 100) // 10), ((cust_number // 100) % 10), (cust_number // 1000) % 10, (cust_number // 10000))
