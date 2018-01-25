#Скрипт на основе if и else, где внутренний код имеет не мение 3-х действий

var1 = int(input("Введите первое число: "))
var2 = int(input("Введите второе число: "))
var3 = int(input("Введите третье число: "))
if var3>var1:
   der = var3-var1
   der = pow(der,2)
   print ("var3 больше var1, их разница в квадрате: ", der)
else:
   sum = var3+var1-var2
   sum = pow(sum,2)
   print ("var3 меньше var1, значение var3 + var1 - var2 в квадрате: ", sum)
  
print ("Good bye! Have a good day!")
