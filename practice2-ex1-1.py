#Скрипт, где если значение переменной больше нуля, то печатается сообщение, в ином случае выполнить операцию суммирования.

n = int(input("Введите число: "))
if n>0:
	print("Введенное число больше нуля")
else:
	m = n + n
	print("Введеное число меньше нуля, операция суммирования n + n: ", m)
