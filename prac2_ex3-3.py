#Парные числа от 0 до 20 и каждое третье от -1 до -21

print ("Парные числа: ")
for x in range (0,21):
    if x !=0 and x % 2 == 0: 
        print (x)

print ("Каждое третье число: ")
for i in range(-1,-22,-2):
   if i !=-1:
     print(i)
