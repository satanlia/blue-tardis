#Создать список из 5 чисел и каждое из них увеличить в 4 раза.

#Первый вариант выполнения 

lst = [1, 2, 3, 4, 5]
answ = [num*3 for num in lst]
print (answ)

#Второй вариант выполнения 
for  i  in  range(len(lst)): 
   lst[i] = lst[i] * 3

print(lst)
