#Создайте 2 списка и присвоить им переменные. Создайте 3 список, где соединяются элементы последовательно с 2 списков: 1212 и вывести ее на экран.

from  random  import  randint

i = 0
j = 0
final = []
list1 = [randint(1, 20)  for  i  in  range(5)] 
list2 = [randint(1, 30)  for  i  in  range(5)]
print (list1)
print (list2)

for l in range(0, 10, 1): #составление конечно списка 
    if l%2!=0 and l!=0:
        final.append(list2[j])
        j=j+1
    else:
        final.append(list1[i])
        i=i+1
print (final)
