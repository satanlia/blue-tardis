#Зашифровать строку в форме SHA512.

import hashlib
h=hashlib.sha224(b'Example')
answ=h.hexdigest()
print("Зашифрованая строка: ", answ)
