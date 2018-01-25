#Генератор паролей с цифр 0-9

import random

pas = ''
for x in range(4): #кол-во символов
    pas = pas + random.choice(list('1234567890'))
print('Привет! Твой пароль: ', pas)
