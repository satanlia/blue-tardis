#Программа с if-elif-else, где количество веток не меньше 4-х

num1 = int(input("Введите x: "))

if num1 == 0:
     result=0
elif num1==1:
     result=1
elif num1==2:
     result=2
elif num1==3:
     result=3
elif num1==4:
     result=4
elif num1==5:
     result=5
else:
     print ("Error")
     result = 0
 
print ("Result: ", result)
