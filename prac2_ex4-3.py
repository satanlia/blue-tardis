#Перепишите программу так, чтобы пользователь решал пример, до тех пор, пока он не напишет правильный ответ (7 попыток).

otv = "FALSE"
i = 0

while otv == "FALSE" and i < 7:
   answ=int(input("5*58-27:"))
   if answ == 263:
     print("YOU WIN")
     otv = "TRUE"
   else:
     print("YOU LOSE")
   i+=1
