#Числа Фибоначчи (до числа 100)

def fibonacci(max_num):
   a, b = 0, 1 
   while a < max_num: 
      yield a 
      a, b = b, a + b 
        
for n in fibonacci(100): 
   print (n)
