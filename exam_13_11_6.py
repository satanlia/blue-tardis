#Задача 13 
import hashlib
h=hashlib.sha224(b'Example')
answ=h.hexdigest()
print("Example in sha224:", answ)

#Задача 11
import hashlib
h1=hashlib.md5(b'World')
answ1=h1.hexdigest()
print("World in md5:",answ1)

#Задача 6
lst = ['yesterday', 'today', 'tomorrow']
for  word  in  lst:   
   print()
   for  letter  in  word:
      print(letter, end="&")
