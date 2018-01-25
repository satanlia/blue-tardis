#Создать функцию def fc1 (num): n = num: 10 print (n) Вызвать эту функцию, где в качестве аргументов - глобальная переменная, число, строка.

globalvar=10

def fc1(globalvar, num, str):
  n=num/10
  print("Ответ:", n)
  print('Глобальная переменная:', globalvar)
  print('Строка:', str)

  
new=fc1(globalvar, 10, "practice4")
