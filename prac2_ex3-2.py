#Фибоначчи с 5-го по 20-й член ряда

fib5 = 3
fib6 = 5
print (fib5)
print (fib6)
n = 18
i = 5
fib_sum = 0
while i < n:
	fib_sum = fib5 + fib6
	print (fib_sum)
	fib5 = fib6
	fib6 = fib_sum
	i = i + 1
