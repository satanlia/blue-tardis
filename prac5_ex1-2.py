#Написать код наличии в модуле math двух идентификаторив- переменных - число Пи и переменная y.

import math

lst=(dir (math)) #считываем список команд модуля в новый список
n=len(lst) #считаем количество элементов
x=(lst.count('pi'))	#считаем сколько раз упоминается
y=(lst.count('y'))	#считаем сколько раз упоминается
if x==1:
  print("В модуле есть индентификатор числа рі")
else: 
  print("В модуле нет индентификатора числа рі")
if y==1:
  print("В модуле есть индентификатор переменной у")
else: 
  print("В модуле нет индентификатора переменной у")
