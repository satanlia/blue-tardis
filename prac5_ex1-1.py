#Написать код, вывода даты по машинному часами системы.

mport datetime
     
today = datetime.datetime.today()
print ("Нормально отредаченая дата: ")
print( today.strftime("%d/%m/%Y") )

#ЕСЛИ НУЖНЫ ДРУГИЕ ФОРМАТЫ ИЛИ МЕТОДЫ
print()
now = datetime.datetime.now()
print ("Текущая дата и время с использованием метода str:")
print (str(now))
print()
print ("Текущая дата и время с использованием атрибутов:")
print ("Текущий год: %d" % now.year)
print()
print ("Текущий месяц: %d"% now.month)
print()
print ("Текущий день: %d" % now.day)
print()
print ("Текущий час: %d" % now.hour)
print()
print ("Текущая минута: %d" % now.minute)
print()
print ("Текущая секунда: %d" % now.second)
print()
print ("Текущая микросекунда: %d" % now.microsecond)
print()
print ("Текущая дата и время с использованием strftime:")
print (now.strftime("%d-%m-%Y %H:%M"))
print()
print ("Текущая дата и время с использованием isoformat:")
print (now.isoformat())
