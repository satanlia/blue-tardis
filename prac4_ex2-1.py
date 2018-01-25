#Написать код, с использованием функций и аргументов, который бы с возвращением к основной программе смог бы рассчитать выражение: (a + b) -c 5 (d)

import math

def func(a,b,c,d):
	answ=(a+b)-(pow(c,5))*d
	return answ
	
def func1(a,b,c,d):
	answ=(a+b)-(pow(c,5))*math.fabs(d)
	return answ
	
	
print(func(5,10,-2,20)) #если d просто в скобках
print(func1(5,10,-2,20)) #если имеется в виду модуль числа d
